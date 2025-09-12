# AI Vision Demo

The ST AI Vision Component is based on our original [AI Vision Demo](https://github.com/avnet-iotconnect/iotc-python-lite-sdk-demos/tree/main/stm32mp157f-dk2/ai-vision)
that was originally created for out [/IOTCONNECT Python Lite SDK](https://github.com/avnet-iotconnect/iotc-python-lite-sdk). 
The demo has been tested with [STM32 MP157f-DK](https://www.st.com/en/evaluation-tools/stm32mp157f-dk2.html)
but should be able to run other MP1 and MP2 devices.

Once a USB UVC-Compliant Camera (such as [this](https://www.amazon.com/ALPCAM-Distortion-Compliant-Embedded-Industrial/dp/B0B1WTV1KB)) 
is connected to the USB A port on the device and component is deployed with IoTConnect, assuming your device
has an HDMI or an LVDS Display connected and can run Weston Graphical User Interface, the screen will show the camera
view, highlight recognizable object on the screen when they are detected and report the recognized object class and confidence 
to /IOTCONNECT.

Download the pre-built component [here](https://downloads.iotconnect.io/greengrass/components/iotc-gg-component-st-ai-vision-1.0.0.zip)