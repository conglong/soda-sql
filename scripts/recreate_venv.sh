#!/usr/bin/env bash
# shellcheck disable=SC2096

set -e -x

# Run this from the root project dir with scripts/recreate_venv.sh

rm -rf $VENV_DIR
rm -rf soda_sql.egg-info

python -m venv .venv
source .venv/Scripts/activate
#pip install --upgrade pip
pip install pip
pip install "$(cat dev-requirements.in | grep pip-tools)"
#pip-compile requirements.in
pip-compile dev-requirements.in
pip install -r requirements.txt
pip install -r dev-requirements.txt
pip install -e core/.
