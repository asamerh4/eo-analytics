#!/bin/bash
set -ex

BUILD=$(git rev-parse --short HEAD)
CLUSTER_NAME="analytics"
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e ${YELLOW}"**building cluster $CLUSTER_NAME"-"$BUILD"${NC}

rm -rf ~/.ansible
python scripts/cluster_deploy.py \
  -z \
  -m \
  -s3 "s3a://s2-sync" \
  -b 800 \
  -k "~/mesos140.pem" \
  -ok mesos140 \
  -u centos \
  eu-central-1 \
  $CLUSTER_NAME"-"$BUILD \
  provision
