#!/bin/bash

set -e

cd "$(dirname "$0")"

if which gdk > /dev/null; then
  python3 -m pip install -U git+https://github.com/aws-greengrass/aws-greengrass-gdk-cli.git@v1.6.2
fi

if [[ -n "$PACKAGE_LOCAL_SDK" ]]; then
  # Optional: Set this value to anything to build and package local SDK source as well.
  ../../scripts/package.sh
  mkdir -p local-packages/
  cp -f ../../dist/*.whl local-packages/
fi

gdk component build

recipe=greengrass-build/recipes/recipe.yaml

echo "Recipe generated at ${recipe}. Upload THIS recipe to /IOTCONNECT"
