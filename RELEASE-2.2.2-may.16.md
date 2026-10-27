# May Status 2.2.2-may.16

Includes the completed May data-contract and migration-fallback cleanup from 2.2.2-may.15. Fix the independent Linux/Windows CI artifact path to the current `may-monitor-theme-status-build-*.zip` name. Version 15's lint, tests and build passed, but its separate CI failed to upload the artifact under the retired filename. Publish a new version without replacing the existing tag or attachments.

Probe-failure charts use count-weighted May `ping.loss` metrics; missing or failed statistics remain missing. Keep the existing `GlassmorphismEnhanced` settings identity, managed appearance settings, lazy chart loading, hidden-page transport lifecycle and network-only PWA resources. Account identities and upstream attribution are unchanged.

This release does not activate the theme in production. Stage the verified ZIP and explicitly select its lock hash in Deploy when an upgrade is authorized.
