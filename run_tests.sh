#!/usr/bin/env bash
set -euo pipefail

# Run pytest using the project's virtualenv Python to avoid relying on shell activation.
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$ROOT_DIR/venv_hivebox/bin/python"

if [ ! -x "$VENV_PY" ]; then
  echo "Virtualenv python not found at: $VENV_PY"
  echo "Activate the venv with: source venv_hivebox/bin/activate or create the venv first."
  exit 1
fi

# Pass all args to pytest
"$VENV_PY" -m pytest "$@"
