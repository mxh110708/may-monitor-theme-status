# May Status 开发与打包

先读[仓库约定](../AGENTS.md)；修改 `src/` 前还需读其局部约定。固定 Bun 1.3.14 和 `bun.lock`，不以浮动安装替代正式输入。当前 Node 声明为 `^20.19.0 || >=22.12.0`。

```bash
bun install --frozen-lockfile
bun run dev
```

开发服务仅为主题前端，不会安装 May Server、创建节点或补造探测。使用自己的隔离后端和测试数据，不能默认指向生产管理会话。

## 验证

```bash
bun run lint
bun run build
bun run check:package
bun run test:package
```

`lint` 带 `--fix --cache`，会改文件，执行后审查差异。`build` 包含类型检查、Vite 构建和包检查。生成 `dist/` 及 `may-monitor-theme-status-build-<commit>.zip`。

已有构建的本地静态预览使用 `package.json` 中的 `preview` 脚本：

```bash
bun run preview
```

静态预览不提供监控后端。真实页面验收还需检查首页、详情、外观、探测历史、缺测、过期、断网、隐藏标签和内置管理路由。

## 包与身份

ZIP 保留 `dist/`、`komari-theme.json` 和 `preview.png`，以及构建要求的 `public/registerSW.js`／`public/sw.js` 原始覆盖字节。这两个 Worker 资源不拦截请求，不用旧 PWA 导航兜底管理页。包检查验证资源、身份与网络行为，不等于完整浏览器测试。

`short=GlassmorphismEnhanced` 是设置技术身份，不能改成品牌名；包与清单版本保持一致。站点默认图标从原始照片直接裁剪缩放，处理及来源见[图标说明](DEFAULT-SITE-ICON.md)，不要用重新生成或调色资源替代。

## 发布和维护

`build-ci.yml` 校验固定依赖、lint 和构建，`release-on-version-bump.yml` 在 main 的版本变化时发行。纯文档修改不增加版本、不覆盖已发附件，也不触发生产安装。版本、来源和资源不一致时应停止打包。

上游协议说明和技术文件名保留，品牌改名不包括用户账号、许可证或随意更改数据键。历史的 Komari 安装／迁移记录不再作为当前安装步骤；当前流程以[使用教程](USER-GUIDE.zh-CN.md)为准。
