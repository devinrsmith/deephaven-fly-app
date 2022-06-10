#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

APP_NAME="${APP_NAME:-dh-${USER}}"
ORG="${ORG:-deephaven-13}"

# Echo, have the first region selected
echo | flyctl launch --copy-config --no-deploy --name "${APP_NAME}" --org "${ORG}"
flyctl scale memory 2048
flyctl deploy --remote-only
flyctl open
