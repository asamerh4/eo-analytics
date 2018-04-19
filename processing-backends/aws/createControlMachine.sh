#!/bin/bash
set -e

BUILD=$(git rev-parse --short HEAD)
CLUSTER_NAME="control"
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e ${YELLOW}"**deploying control Machine..."${NC}
echo "###########"
echo "#IMPORTANT#"
echo "###########"
echo "#EXECUTE ONLY FROM YOUR PERSONAL LINUX HOST WHERE YOUR SECURE SSH-KEYS ARE STORED!"

rm -rf ~/.ansible
python \
 scripts/createControlMachine.py \
 -k "~/controlMachine.pem" \
 -ck "~/mesos140.pem" \
 -ok controlMachine \
 -ock mesos140 \
 -u centos \
 eu-central-1 \
 $CLUSTER_NAME"-"$BUILD