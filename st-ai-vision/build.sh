#!/bin/bash

set -e

cd "$(dirname "$0")"

if ! which gdk > /dev/null; then
  python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
fi

gdk component build
