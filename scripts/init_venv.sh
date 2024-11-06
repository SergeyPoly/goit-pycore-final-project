#!/bin/sh

rootdir="$(dirname -- "$( readlink -f -- "$0"; )")/.."

python3 -m venv $rootdir/.venv
source $rootdir/.venv/bin/activate
pip install -r $rootdir/requirements.txt