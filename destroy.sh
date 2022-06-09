#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

APP_NAME="${APP_NAME:-dh-${USER}}"

flyctl apps destroy "${APP_NAME}"
