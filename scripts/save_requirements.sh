#!/bin/sh

rootdir="$(dirname -- "$( readlink -f -- "$0"; )")/.."

pip freeze > $rootdir/requirements.txt