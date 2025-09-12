#!/bin/bash

set -e

cd "$(dirname "$0")"/..

source ~/.venv-proteus-ble-demo/bin/activate
python3 -u proteus-ble.py "$@"
