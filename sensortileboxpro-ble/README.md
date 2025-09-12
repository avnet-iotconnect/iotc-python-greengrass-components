# SensorTile Box Pro BLE Demo

This demo runs a python application inside a Greengrass-Light component on a STM32MP157F-DK2, STM32MP135F-DK, or 
STM32MP257F-DK to receive various data points from the ST SensorTileBox Pro sensor pack and then send that data as 
telemetry to the IoTConnect cloud platform.

The `sensortile-template.json` template in this directory should be used to register the greengrass device in IOTCONNECT.

Here are the data fields that are reported:

* temperature_deg_C
* battery_percentage
* battery_voltage
* battery_current
* battery_status
* accel_x_mGs
* accel_y_mGs
* accel_z_mGs
* gyro_x_dps
* gyro_y_dps
* gyro_z_dps
* magnet_x_mGa
* magnet_y_mGa
* magnet_z_mGa
* pressure_mBar

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-sensortileboxpro-ble-1.0.0.zip)

## Preparing SensorTileBox Pro Sensor Pack

Begin by powering your SensorTileBox Pro Sensor pack with 5VDC using a USB-C cable, and turning the power switch to the 
"ON" position.

On a smartphone (IOS or Android), install the ST BLE Sensor App. Turn your phone's bluetooth on, and then open the app. 
The SensorTileBox Pro module should be discovered under the name "BLEPnP". If not, refresh the page until it is.

If a firmware upgrade is available for your SensorTileBox Pro, you should be automatically prompted to flash the newly 
available firmware. After it has finished flashing, reboot the SensorTileBox Pro and reconnect to it in the app to 
verify that the firmware flash was successful.

Your SensorTileBox Pro should now be ready for use.
