#!/bin/bash

set -ex

BUILD=$(git rev-parse --short HEAD)
CLUSTER_NAME="template"
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e ${YELLOW}"**building analytics machine Image..."${NC}

rm -rf ~/.ansible
python scripts/otc_create_machine_image.py \
 -k "~/mesos130-api.pem" \
 -ok mesos130-api \
 -u linux \
 eu-de