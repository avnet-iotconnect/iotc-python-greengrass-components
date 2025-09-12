#!/bin/bash

set -e

# Should suppress some of the "Inappropriate ioctl for device" messages.
export DEBIAN_FRONTEND=noninteractive

apt update -y
apt install -y x-linux-ai-tool

# Try install NPU package (should install on MP2) and then CPU if failed
# NOTE: We have to to assume that all MP2s will support the NPU demo,
# as we don't have a reliable way to predict compatibility reliably
x-linux-ai -i packagegroup-x-linux-ai-demo-npu || x-linux-ai -i packagegroup-x-linux-ai-demo-cpu
systemctl restart weston-graphical-session.service
