# May Status

面向 May Monitor 的公开状态主题，用节点总览、历史图表和线路质量展示真实监测结果。支持毛玻璃外观、可配置卡片与列表、地图及背景；它不承担后台鉴权、Agent 采集或代理故障切换。

[English](README.en.md) · [发行版](https://github.com/mxh110708/may-monitor-theme-status/releases/latest) · [安装与外观](docs/USER-GUIDE.zh-CN.md) · [网络数据口径](docs/NETWORK-DATA.zh-CN.md) · [文档目录](docs/README.md)

## 版本与配套

当前文档基线为 **2.2.2-may.17**，对应 May Monitor **0.1.0** 的 RPC2、状态及 `ping.loss` 合同。主题、Server 和内置 Web 的版本独立；旧 Komari 的全部版本不在当前新增适配范围。

May Status 只接管公开展示。管理、初始化和恢复继续由 [May Monitor Web](https://github.com/mxh110708/may-monitor-web) 提供。普通使用无需安装开发工具；维护者通过固定 ZIP、SHA-256 和主题锁启用代码，不开启通用主题市场或任意脚本扩展。

## 功能

- 卡片／列表、总览指标组合、快捷筛选与自定义节点顺序，区分等待、在线、离线、过期和未知状态。
- 节点详情与主机历史，CPU 百分比与系统负载分轴，不把 load 当作百分比。
- 按任务、运营商和地址族展示实际延迟与探测失败比例；缺测留空，100% 失败照实显示。
- 可选地理距离评级，未知或冲突位置保持中性，不用服务器历史为绕路放宽标准。
- 后台「May Status 外观」配置主题模式、刷新、首页模块、地图、卡片、图标和背景。
- 默认 HTTP 读取，可显式选择 WebSocket；页面隐藏暂停实时读取，恢复可见后读取当前状态。
- 原始梅花照片裁剪的默认图标，支持本地上传或明确配置外部图标。

## 使用流程

1. 先确保 May Monitor Server、真实 Agent 和需要展示的探测任务已正常运行。
2. 由维护者核对本主题固定发行附件与 SHA-256，使用本仓库的暂存脚本生成不可覆盖的锁修订。
3. 在配套 Deploy 中选择已核对的 Server，应用受审静态主题锁；先做一致性备份，再切换和验证。
4. 在后台配置「May Status 外观」，检查公开字段、首页、节点详情、历史、未知状态和管理入口。

完整参数、暂存脚本来源、更新、恢复及故障处理见[使用教程](docs/USER-GUIDE.zh-CN.md)。保存外观不是安装新主题代码，主题更新也不授予修改 Cloudflare、Tunnel、代理或 SSH 的权限。

## 如何读网络图表

延迟保留原始测量，不除以二、不按历史归一化。地理评级依据机房与任务目标的城市参考点和统一公式，是主题显示策略，不是行业 SLA，也不是 Route 的分区切换阈值。

丢包视图使用 `ping.loss` 时间桶的失败比例，按探测次数加权。它代表探测失败率，不等于所有业务包的丢包率。**缺少该指标或接口不兼容时显示不可用，不回退估算，不从降采样延迟推算。** 图表选择七天仍受 Server 的实际保留粒度与范围限制。详见[网络数据口径](docs/NETWORK-DATA.zh-CN.md)。

## 开发

固定使用 Bun **1.3.14**；当前 Node 范围为 `^20.19.0 || >=22.12.0`。从仓库根目录执行：

```bash
bun install --frozen-lockfile
bun run dev
```

构建和打包检查见[开发与验证](docs/DEVELOPMENT.zh-CN.md)。`bun run lint` 会自动修复并写缓存，需审查差异；不要把它当作只读文档检查。构建生成 `dist/` 与 `may-monitor-theme-status-build-<commit>.zip`，必须保留清单、预览和两个网络模式 PWA 覆盖资源。

技术栈为 Vue 3、Vite、Pinia、reka-ui、Tailwind CSS v4、ECharts 及地图组件。构建检查不证明所有浏览器、真实数据和生产恢复都已验收。

## 来源、许可与反馈

May Status 是独立维护的衍生主题，感谢 [Komari](https://github.com/komari-monitor/komari)、[Glassmorphism Enhanced](https://github.com/jianmomo/komari-theme-Glassmorphism-Enhanced)、[Glassmorphism](https://github.com/sanrokamlan-prog/komari-theme-Glassmorphism)、Komari Emerald 及 [Komari Naive](https://github.com/tonyliuzj/komari-naive) 的设计与实现。保留 [MIT 许可证](LICENSE) 和上游版权声明。

`komari-theme.json` 是格式名，`GlassmorphismEnhanced` 是已保存设置的技术身份，不能为改名盲目替换。反馈附 Server／主题版本、浏览器、发生时间及脱敏截图；不提交数据库、Token、完整私有配置或备份。
