#!/bin/sh

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

cd "$parent_path/.."

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt