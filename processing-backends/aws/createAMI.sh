#!/bin/bash

set -ex

BUILD=$(git rev-parse --short HEAD)
CLUSTER_NAME="template"
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e ${YELLOW}"**building analytics machine Image..."${NC}

rm -rf ~/.ansible
python \
 scripts/createAnalyticsAMI.py \
 -k "/home/dev1/mesos140.pem" \
 -ok mesos140 \
 -u centos \
 eu-central-1 \
 $CLUSTER_NAME"-"$BUILD