/** May Monitor's data contract: failed requests never fall back to obsolete APIs. */
import type { PingTask } from '@/utils/api'
import type { Client, NodeStatus, PingLossMetricsResponse, PingRecord, StatusRecord } from '@/utils/rpc'
import { getPingLossWindowMs } from '@/utils/pingChartHelper'
import { getSharedRpc } from '@/utils/rpc'

export interface CompatiblePingTask extends PingTask { type?: string, default_on?: boolean }
export interface CompatiblePingRecordsResponse { records: PingRecord[], tasks: CompatiblePingTask[] }
export interface CompatibleLoadRecordsResponse { records: StatusRecord[] }
export interface CompatibleNodesSnapshot { clients: Record<string, Client>, statuses: Record<string, NodeStatus> }

export async function checkMonitorHealth(timeout = 5000): Promise<void> {
  const controller = new AbortController()
  const timer = setTimeout(() => controller.abort(), timeout)
  try {
    const response = await fetch('/ping', { signal: controller.signal, cache: 'no-store' })
    if (!response.ok || (await response.text()).trim() !== 'pong')
      throw new Error(`Unexpected health response: ${response.status}`)
  }
  finally { clearTimeout(timer) }
}

export async function getMonitorNodesSnapshot(): Promise<CompatibleNodesSnapshot> {
  const rpc = getSharedRpc()
  const [clients, statuses] = await Promise.all([rpc.getNodes(), rpc.getNodesLatestStatus()])
  if (!clients || !statuses || typeof clients !== 'object' || typeof statuses !== 'object')
    throw new TypeError('Invalid May Monitor snapshot')
  return { clients, statuses }
}

export function normalizeRpcLoadRecords(records: unknown, uuid: string): StatusRecord[] {
  const source = Array.isArray(records) ? records : records && typeof records === 'object' ? (records as Record<string, unknown>)[uuid] : []
  if (!Array.isArray(source))
    throw new TypeError('Invalid May Monitor history')
  return source.filter((record): record is StatusRecord => Boolean(record && typeof record === 'object'
    && typeof record.time === 'string' && Number.isFinite(new Date(record.time).getTime()) && Number.isFinite(record.cpu)))
}

export async function getMonitorLoadRecords(uuid: string, hours: number): Promise<CompatibleLoadRecordsResponse> {
  const result = await getSharedRpc().getLoadRecords(uuid, hours)
  return { records: normalizeRpcLoadRecords(result?.records, uuid) }
}

export async function getMonitorPingRecords(uuid: string | undefined, hours: number): Promise<CompatiblePingRecordsResponse> {
  const result = await getSharedRpc().getClient().call<CompatiblePingRecordsResponse>('common:getRecords', { type: 'ping', uuid, hours })
  if (!Array.isArray(result?.records) || !Array.isArray(result?.tasks))
    throw new TypeError('Invalid May Monitor probe history')
  return result
}

let lossRetryAt = 0
export async function getMonitorPingLossMetrics(uuid: string, hours: number, until: number): Promise<PingLossMetricsResponse | null> {
  if (Date.now() < lossRetryAt)
    return null
  const step = getPingLossWindowMs(hours)
  const start = Math.floor((until - hours * 3_600_000) / step) * step
  try {
    const result = await getSharedRpc().getClient().call<PingLossMetricsResponse>('public:queryMetrics', {
      metric_keys: ['ping.loss'],
      entity_ids: [uuid],
      start: new Date(start).toISOString(),
      end: new Date(until).toISOString(),
      max_points: Math.ceil((until - start) / step),
      aggregation: 'avg',
      fill_empty: true,
    })
    if (!Array.isArray(result?.series))
      throw new TypeError('Invalid May Monitor ping.loss response')
    lossRetryAt = 0
    return { series: result.series.filter(series => series.metric_key === 'ping.loss' && series.entity_id === uuid && Array.isArray(series.points)) }
  }
  catch {
    lossRetryAt = Date.now() + 60_000
    return null
  }
}
