# PROTEUS BLE Demo

This demo runs a python application inside a Greengrass-Light component on a STM32MP157F-DK2, STM32MP135F-DK, or 
STM32MP257F-DK to receive various data points from the ST PROTEUS sensor pack and then send that data as telemetry to 
the IoTConnect cloud platform.

The `GGproteus-template.json` template in this directory should be used to register the greengrass device in IOTCONNECT.

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
* rms_speed_status_x
* rms_speed_status_y
* rms_speed_status_z
* rms_speed_x_mmps
* rms_speed_y_mmps
* rms_speed_z_mmps
* freq_status_x
* freq_status_y
* freq_status_z
* freq_x_hz
* freq_y_hz
* freq_z_hz
* freq_max_amp_x_ms2
* freq_max_amp_y_ms2
* freq_max_amp_z_ms2
* accel_peak_status_x
* accel_peak_status_y
* accel_peak_status_z
* accel_peak_x_ms2
* accel_peak_y_ms2
* accel_peak_z_ms2

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-proteus-ble-1.0.0.zip)

## Preparing PROTEUS Sensor Pack

To prepare your ST PROTEUS pack for the demo, you will need to make sure it is loaded with the correct firmware file 
(`STSW-PROTEUS_1_1_1.bin` available in this directory). Since the firmware flashing will be done from a smartphone, you 
will need to send and save this file to your smartphone (email is probably the easiest way). 

After assembling your PROTEUS sensor module, power it on using a micro-usb cable.

On a smartphone (IOS or Android), install the ST BLE Sensor App. Turn your phone's bluetooth on, and then open the app. 
The PROTEUS module should be discovered. If not, refresh the page until it is.

After tapping on your PROTEUS in the device discovery screen, tap on the gear icon in the top-right of your screen, and 
then "Firmware Upgrade" in the resulting pop-up. Tap on the blue folder icon, select the `STSW-PROTEUS_1_1_1.bin` file, 
and then tap the "UPGRADE" button to flash the firmware.

After the flash has completed, the PROTEUS will automatically reboot and you can close out of the app on your phone.

>[!NOTE]
>Before connecting the PROTEUS to a new device, it is advised to manually reboot the sensor pack to ensure it is not 
> still connected to another device. Using a small blunt pin or screwdriver, press and hold the S2 power switch down for 
> 3 seconds. If you have the device sitting right-side-up on a desk with the Micro-USB connector facing to your left, 
> the S2 button will be accessed through the only slot in the plastic casing that is facing you.

