#!/bin/bash

set -e

cd "$(dirname "$0")"/..

sources_root="$(pwd)"

export XDG_RUNTIME_DIR="/run/user/$(id -u)"
export WAYLAND_DISPLAY="wayland-0"

wayland_socket="${XDG_RUNTIME_DIR}/${WAYLAND_DISPLAY}"
echo "Waiting for Wayland socket at ${wayland_socket}..."
until [ -S "${wayland_socket}" ]; do
  sleep 2
done
echo "Wayland socket ready, launching demo."

if [[ -f /usr/local/x-linux-ai/resources/config_board_npu.sh ]]; then
  source /usr/local/x-linux-ai/resources/config_board_npu.sh
else
  source /usr/local/x-linux-ai/resources/config_board_cpu.sh
fi
source ~/.venv-st-ai-vision/bin/activate
export PYTHONPATH=$PYTHONPATH:/usr/local/x-linux-ai/object-detection
#cd /usr/local/x-linux-ai/object-detection
python3 -u "${sources_root}/st-ai-vision.py" \
  -m /usr/local/x-linux-ai/object-detection/models/$OBJ_DETEC_MODEL \
  -l /usr/local/x-linux-ai/object-detection/models/$OBJ_DETEC_MODEL_LABEL.txt \
  --framerate $DFPS --frame_width $DWIDTH --conf_threshold 0.7 --frame_height $DHEIGHT $OPTIONS
