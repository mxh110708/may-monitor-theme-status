# May Status 文档

基线：主题 2.2.2-may.17 + May Monitor 0.1.0。中文为主，[English overview](../README.en.md) 与 [English guide](USER-GUIDE.en.md) 提供英文说明。

## 当前教程

1. [首页](../README.md)：职责、功能及配套范围。
2. [安装、外观、更新与恢复](USER-GUIDE.zh-CN.md)。
3. [网络数据与评级](NETWORK-DATA.zh-CN.md)：延迟原值、失败比例、位置和粒度。
4. [开发与验证](DEVELOPMENT.zh-CN.md)、[默认图标](DEFAULT-SITE-ICON.md)。

## 历史与实现参考

以下文件描述各自日期的实现和验收，不是当前安装步骤。旧候选「尚未发布」与旧回退策略均按当时事实解释，不能拿来覆盖当前接口合同。

- [May 全新安装迁移（2026-10-20）](BRAND-MIGRATION-2026-10-20.zh-CN.md)。
- [CPU 与系统负载图表说明](CPU-AXIS-2026-10-16.zh-CN.md)。
- [PWA 源码与构建一致性维护](MAINTENANCE-2026-10-02.zh-CN.md)。
- [May Monitor 适配与项目改名](MAY-MONITOR-2026-10-26.zh-CN.md)。
- [详情页丢包曲线修复与验证](PING-LOSS-2026-10-16.zh-CN.md)。

更长的实现沿革见 [May-CUSTOM](../May-CUSTOM.md)。固定清单技术身份与版权不做品牌替换；当前不回退旧 REST、不估算缺失的 `ping.loss`。
