# May Status 2.2.2-may.15

May Monitor public theme with the reviewed M9 API adaptation and pinned static deployment. Remove obsolete API compatibility paths and use the May data contract directly. Probe-failure charts use count-weighted `ping.loss` metrics; missing or failed statistics remain missing instead of falling back to a ratio of sampled latency records.

Keep the existing `GlassmorphismEnhanced` theme settings identity, appearance settings, lazy chart loading, hidden-page transport lifecycle and network-only PWA resources. `komari-theme.json` is the retained package schema filename; upstream attribution and account identities are unchanged.

Use with the reviewed May Server/Web pair. Uploading or publishing the theme does not activate it in production. Stage the verified ZIP and explicitly select its lock hash in Deploy when an upgrade is authorized.
