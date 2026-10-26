#!/usr/bin/env bash
set -euo pipefail
# A content-pinned static bundle is staged independently of service activation.
# May Deploy owns activation, its component backup and recovery transaction.
exec python3 "$(dirname -- "${BASH_SOURCE[0]}")/stage-reviewed-theme.py" "$@"