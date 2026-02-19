# About

This repository holds a collection of Components based on the 
[/IOTCONNECT Greengrass SDK for Python-Based Components](https://github.com/avnet-iotconnect/iotc-python-greengrass-sdk)
that can be deployed to devices running an AWS Greengrass Nucleus with /IOTCONNECT. 
To learn more about more basic component examples, about the SDK itself 
or how your build your Greengrass SDK Component with /IOTCONNECT, visit the above SDK GitHub page link.

# Before Running The Demos

Please learn about how to use /IOTCONNECT to deploy a Greengrass Nucleus at the 
[iotc-python-greengrass-sdk](https://github.com/avnet-iotconnect/iotc-python-greengrass-sdk)
page and follow the steps to ensure that:
* Your /IOTCONNECT Device Template is created.
* Your Device created in /IOTCONNECT and is Running the Greengrass Nucleus.
* Your Component is built and registered in /IOTCONNECT.
* Your Firmware is created.
* The demo component from this repo is deployed to your device.

# AI Vision Demo

This demo integrates with the code provided by ST and can detect objects by using the camera   
connected to the device. The list of trained objects is provided in
[this list](https://github.com/avnet-iotconnect/iotc-python-lite-sdk-demos/blob/main/stm32mp157f-dk2/ai-vision/object-labels.txt).

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-st-ai-vision-1.0.2.zip)

# PROTEUS BLE Demo

This demo reads and decodes BLE data transferred by the STEVAL-PROTEUS1 Sensor Pack before packaging up the data as 
telemetry and sending it to /IOTCONNECT. The data includes fields regarding the battery health of the PROTEUS as well 
as acceleration, gyroscope, temperature, and frequency readings.

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-proteus-ble-1.0.0.zip)

# SensorTileBox Pro BLE Demo

This demo reads and decodes BLE data transferred by the ST SensorTileBox Pro Sensor Pack before packaging up the data 
as telemetry and sending it to /IOTCONNECT. The data includes fields regarding the battery health of the SensorTileBoxPro 
as well as acceleration, gyroscope, temperature, magnetic field, and pressure readings.

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-sensortileboxpro-ble-1.0.0.zip)
