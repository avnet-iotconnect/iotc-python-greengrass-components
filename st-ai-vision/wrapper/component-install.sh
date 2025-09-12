#!/bin/bash

set -e
set -x

cd "$(dirname "$0")"/..

# NOTE: This takes about 60 seconds on some STM32 MP1 devices. Tune the recipe timeout if we need more time.
python3 -m venv --system-site-packages ~/.venv-st-ai-vision

source ~/.venv-st-ai-vision/bin/activate


if [ "$(df --output=avail /tmp | tail -n 1)" -lt 524288 ];
  # Some STM32 MPx devices have 256 MB /tmp or less, and that's not enough to install awscrt (dependency of awsiotsdk)
  then echo "Detected less than 512MB available on /tmp. Applying a workaround for pip install."
  mkdir -p ~/tmp || :
  export TMPDIR=~/tmp
fi

python3_opts=
if [[ -d /var/cache/iotconnect/wheelhouse ]]; then
     python3_opts=--find-links=file:///var/cache/iotconnect/wheelhouse
fi

# for others, let's not have the warning printed for non-existing dir
# shellcheck disable=SC2086
python3 -m pip install $python3_opts -r requirements.txt

if [ -n "$TMPDIR" ]; then
  rm -rf ~/tmp
  unset TMPDIR # for any future changes down below this line
fi

echo Done.
