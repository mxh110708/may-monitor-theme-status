# May Status

A public status theme for May Monitor, displaying node summaries, host history and probe quality. It provides configurable cards/lists, glass-style appearance, maps and backgrounds; it is not an administration server, Agent or proxy failover controller.

[简体中文](README.md) · [Releases](https://github.com/mxh110708/may-monitor-theme-status/releases/latest) · [User guide](docs/USER-GUIDE.en.md) · [Documentation](docs/README.md)

The baseline is **2.2.2-may.17**, paired with May Monitor **0.1.0** and its RPC2/status/`ping.loss` contracts. Administration, setup and recovery keep using the embedded May Monitor Web UI. General compatibility with old Komari releases is not promised.

## Features and data

- Configurable overview metrics, cards/lists, quick filters and node ordering.
- Distinct first-report waiting, online, offline, stale and unknown states.
- CPU percentage and system load on separate axes.
- Real probe latency and failure ratios, with missing data left missing.
- Optional geographic display ratings from city reference points and one shared formula; unknown/conflicting locations are not guessed.
- Managed appearance, default plum-blossom icon, uploaded/explicit external icons and optional backgrounds.
- HTTP by default, optional WebSocket and paused live reading while hidden.

Latency is not divided by two or normalized against a node's history. Geographic ratings are a display policy, not an SLA or May Route's failover thresholds. Probe failure ratio is not general application packet loss. Loss charts use count-weighted `ping.loss` buckets; unavailable capability stays unavailable, without estimation from downsampled latency. Requested history remains limited by the Server's retention and resolution.

## Install

First verify a working May Monitor Server, real Agents and probe tasks. Review the fixed theme Release and checksum, stage it using this repository's script, then activate the resulting lock through Deploy's component-scoped maintenance. Do not enable arbitrary extensions or use a generic upstream marketplace workflow.

The [English guide](docs/USER-GUIDE.en.md) and [Chinese manual](docs/USER-GUIDE.zh-CN.md) cover staging, appearance, validation and recovery. Settings changes do not install new code. Static theme JavaScript is trusted same-origin code, not a browser security sandbox.

## Develop

Use Bun **1.3.14** and the committed lockfile:

```bash
bun install --frozen-lockfile
bun run dev
bun run build
bun run check:package
bun run test:package
```

`bun run lint` additionally fixes files and writes a cache; review its diff. See [development](docs/DEVELOPMENT.zh-CN.md) before packaging. Preserve the manifest, preview and both network-only PWA overrides. A package check is not real-browser acceptance.

Derived from Komari and the Glassmorphism theme family, with retained [MIT license](LICENSE) and upstream attribution in the [Chinese overview](README.md). `komari-theme.json` and `short=GlassmorphismEnhanced` are format/settings identities, not migration shims. Report exact versions and redacted reproduction evidence, without credentials or private databases.
