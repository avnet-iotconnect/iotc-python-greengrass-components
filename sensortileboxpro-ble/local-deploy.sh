#!/bin/bash

set -e

cd "$(dirname "$0")"

./build.sh "$@"

sudo -E /greengrass/v2/bin/greengrass-cli \
  component details --name "io.iotconnect.example.IotConnectSdkSensorTileBoxProBleDemo" | true

sudo -E /greengrass/v2/bin/greengrass-cli \
  deployment create \
  --remove "io.iotconnect.example.IotConnectSdkSensorTileBoxProBleDemo" | true

sudo -E /greengrass/v2/bin/greengrass-cli \
  deployment create \
  --recipeDir greengrass-build/recipes \
  --artifactDir greengrass-build/artifacts \
  --merge "io.iotconnect.example.IotConnectSdkSensorTileBoxProBleDemo=1.0.0"

exit 0
