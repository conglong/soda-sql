#!/usr/bin/env bash
# shellcheck disable=SC2096

# Run this from the root project dir with scripts/run_all_tests.sh

source .venv/Scripts/activate

python -m pytest tests/local
