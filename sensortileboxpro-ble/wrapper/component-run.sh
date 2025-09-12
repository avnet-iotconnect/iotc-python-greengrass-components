#!/bin/bash

set -e

cd "$(dirname "$0")"/..

source ~/.venv-sensortileboxpro-ble-demo/bin/activate
python3 -u sensortileboxpro-ble.py "$@"
