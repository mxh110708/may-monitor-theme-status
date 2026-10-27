# Installation and appearance

Baseline: May Status 2.2.2-may.17, May Monitor 0.1.0 and Deploy 0.9.38. A source checkout, a built ZIP and an active production lock are different states.

## Stage and activate

1. Verify the Server, real Agents and probe tasks. Save a component-consistent backup and the current theme lock.
2. Select a reviewed theme Release and compare the ZIP's SHA-256 and manifest.
3. Use the staging scripts from **this theme repository**, including the adjacent Python helper. From its root on the managed Linux host:

```bash
sudo bash scripts/install-may-theme-update.sh '<THEME_PACKAGE.zip>' '<PACKAGE_SHA256>'
```

The Python 3 staging helper validates the archive and writes an immutable root-owned revision under `/usr/local/share/may-monitor/themes/<lock-sha256>/`. It reports the lock digest without restarting services or editing databases/DNS.

4. In Deploy, select the verified Server and apply the reviewed static-theme lock. The lifecycle verifies all files, takes a snapshot and restarts only that Server.
5. Verify public home/detail pages, real history, missing/stale/authentication states and the embedded administration route. A 200 HTML fallback does not prove that a JS/CSS asset loaded.

Do not enable general extensions, upload arbitrary HTML or patch compressed administration JavaScript. Static theme code is trusted same-origin code, not a sandbox.

## Configure

Use the managed May Status appearance form. Automatic mode follows Beijing time, light from 07:00 through 18:59. Default refresh is three seconds, configurable from 1–60; it does not alter Agent sampling. HTTP is default; WebSocket requires proxy upgrade support.

Choose cards/lists, overview presets, quick filters, ordering, globe/map, reduced animation and optional backgrounds. Hiding an admin link or prices changes presentation, not server authorization. Review public node/field visibility separately.

The default icon is a direct original-color plum-photo crop. Explicit external icon settings take precedence over an uploaded site icon, then the bundled default. External assets and optional visitor/exchange-rate features can make corresponding network requests.

## Interpret and maintain

Probe latency stays unchanged. Geographic colors are a shared display heuristic, not an SLA or Route failover setting. Unknown/conflicting locations stay neutral. Failure ratios come from count-weighted `ping.loss`; missing capability stays unavailable, without estimation. A seven-day selector does not guarantee seven days of retained detail.

Hidden pages pause live requests and resume with current state. The Server's collection and alerts continue independently.

Updates require a new version and lock; never overwrite a pinned revision. Restoring the embedded UI keeps nodes, history, read access, settings and old resources. Keep any lock still referenced by a recovery point. Browser Worker updates follow browser timing; clearing all user cache is not a normal update step.

See the [full Chinese guide](USER-GUIDE.zh-CN.md), [network semantics](NETWORK-DATA.zh-CN.md) and [development guide](DEVELOPMENT.zh-CN.md). Provide exact versions and redacted evidence for issues, without credentials or private databases.
