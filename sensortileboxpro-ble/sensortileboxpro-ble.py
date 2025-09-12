# SPDX-License-Identifier: MIT
# Copyright (C) 2025 Avnet
# Authors: Zackary Andraka <zackary.andraka@avnet.com> et al.

import sys
import time
import threading
import asyncio
from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
import pexpect
from typing import Optional



from avnet.iotconnect.sdk.greengrass import Client, C2dCommand, Callbacks
from avnet.iotconnect.sdk.sdklib.mqtt import C2dAck


telemetry = {
    "temperature_deg_C":0,
    "battery_percentage":0,
    "battery_voltage":0,
    "battery_current":0,
    "battery_status": "Not_Available",
    "accel_x_mGs":0,
    "accel_y_mGs":0,
    "accel_z_mGs":0,
    "gyro_x_dps":0,
    "gyro_y_dps":0,
    "gyro_z_dps":0,
    "magnet_x_mGa":0,
    "magnet_y_mGa":0,
    "magnet_z_mGa":0,
    "pressure_mBar":0
}


telemetry_lock = threading.Lock()


temperature_pressure_characteristic = "00140000-0001-11e1-ac36-0002a5d5c51b"
accel_gyro_magnet_characteristic =  "00e00000-0001-11e1-ac36-0002a5d5c51b"
battery_characteristic = "00020000-0001-11e1-ac36-0002a5d5c51b"


def on_command(msg: C2dCommand):
    print("Received command", msg.command_name, msg.command_args, msg.ack_id)
    if msg.command_name == "set-user-led":
        if len(msg.command_args) == 3:
            # pretend that we actually RGB values
            status_message = "Setting User LED to R:%d G:%d B:%d" % (int(msg.command_args[0]), int(msg.command_args[1]), int(msg.command_args[2]))
            c.send_command_ack(msg, C2dAck.CMD_SUCCESS_WITH_ACK, status_message)
            print(status_message)
        else:
            c.send_command_ack(msg, C2dAck.CMD_FAILED, "Expected 3 arguments")
            print("Expected three command arguments, but got", len(msg.command_args))
    else:
        print("Command %s not implemented!" % msg.command_name)
        # You can send a failure ack for unrecognised commands, but other components may be servicing those commands,
        # so we should not do this for Greengrass unless we know that we will be the only /IOTCONNECT component running
        #
        # if msg.ack_id is not None:  # it could be a command without "Acknowledgement Required" flag in the device template
        #    c.send_command_ack(msg, C2dAck.CMD_FAILED, "Not Implemented")


def setup_bluetooth():
    setup_process = pexpect.spawn('bluetoothctl', encoding='utf-8')
    setup_process.expect('#')
    setup_process.sendline('power off')
    time.sleep(1)
    setup_process.sendline('power on')
    time.sleep(1)
    setup_process.close()


def temperature_pressure_data_handler(characteristic: BleakGATTCharacteristic, data:bytearray):
    global telemetry
    telemetry["pressure_mBar"] = int.from_bytes(data[2:6], "little")/100.0
    telemetry["temperature_deg_C"] = int.from_bytes(data[6:8], "little")/10.0


def battery_data_handler(characteristic: BleakGATTCharacteristic, data:bytearray):
    global telemetry
    telemetry["battery_percentage"] = int.from_bytes(data[2:4], "little")/10.0
    telemetry["battery_voltage"] = int.from_bytes(data[4:6], "little")/1000.0
    telemetry["battery_current"] = int.from_bytes(data[6:8], "little")
    status_options = ["Low Battery", "Discharging", "Plugged not Charging", "Charging", "Unknown"]
    telemetry["battery_status"] = status_options[data[8]]



def accel_gyro_magnet_data_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    global telemetry
    telemetry["accel_x_mGs"] = int.from_bytes(data[2:4], "little", signed=True)
    telemetry["accel_y_mGs"] = int.from_bytes(data[4:6], "little", signed=True)
    telemetry["accel_z_mGs"] = int.from_bytes(data[6:8], "little", signed=True)
    telemetry["gyro_x_dps"] = int.from_bytes(data[8:10], "little", signed=True)
    telemetry["gyro_y_dps"] = int.from_bytes(data[10:12], "little", signed=True)
    telemetry["gyro_z_dps"] = int.from_bytes(data[12:14], "little", signed=True)
    telemetry["magnet_x_mGa"] = int.from_bytes(data[14:16], "little", signed=True)
    telemetry["magnet_y_mGa"] = int.from_bytes(data[16:18], "little", signed=True)
    telemetry["magnet_z_mGa"] = int.from_bytes(data[18:20], "little", signed=True)



async def sensortileboxpro_setup():
    setup_bluetooth()
    print('starting scan...')
    device = await BleakScanner.find_device_by_name("BLEPnP")
    if device is None:
        print('ERROR: could not find sensortileboxpro device')
        return
    print('Connecting to device...')
    async with BleakClient(device) as client:
        print('Connected')
        await client.start_notify(accel_gyro_magnet_characteristic, accel_gyro_magnet_data_handler)
        await client.start_notify(temperature_pressure_characteristic, temperature_pressure_data_handler)
        await client.start_notify(battery_characteristic, battery_data_handler)
        while True:
            await asyncio.sleep(1)


def sensortileboxpro_loop():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(sensortileboxpro_setup())
    except Exception as e:
        print(f"[sensortileboxpro_loop] Exception: {e}")
    finally:
        asyncio.get_event_loop().close()


def start_sensortileboxpro_thread():
    global sensortileboxpro_thread
    sensortileboxpro_thread = threading.Thread(target=sensortileboxpro_loop, daemon=True)
    sensortileboxpro_thread.start()


# ----------- MAIN ------------
sensortileboxpro_thread: Optional[threading.Thread] = None
start_sensortileboxpro_thread()

try:
    c = Client(
        callbacks=Callbacks(
            command_cb=on_command
        )
    )
    last_check_time = time.time()

    while True:
        # Send telemetry
        with telemetry_lock:
            current_telemetry = telemetry.copy()
        c.send_telemetry(current_telemetry)

        # Every 60 seconds, check if thread is alive
        now = time.time()
        if now - last_check_time >= 60:
            last_check_time = now
            if not sensortileboxpro_thread.is_alive():
                print("[main] sensortileboxpro thread not running. Restarting...")
                start_sensortileboxpro_thread()

        time.sleep(3)

except Exception as e:
    print(e)
    if sensortileboxpro_thread and sensortileboxpro_thread.is_alive():
        sensortileboxpro_thread.join()
    sys.exit(1)

except KeyboardInterrupt:
    print('Exiting.')
    if sensortileboxpro_thread and sensortileboxpro_thread.is_alive():
        sensortileboxpro_thread.join()
    sys.exit(0)
