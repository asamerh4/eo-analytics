#!/bin/bash

BUILD=$(git rev-parse --short HEAD)
CLUSTER_NAME="geomesa-testbed"
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e ${YELLOW}"**destroying cluster $CLUSTER_NAME"-"$BUILD"${NC}

echo "**delete AS-group if any"
aws autoscaling delete-auto-scaling-group --force-delete --auto-scaling-group-name $CLUSTER_NAME-$BUILD-agents --region eu-central-1

echo "**delete LC if any"
aws autoscaling delete-launch-configuration --launch-configuration-name $CLUSTER_NAME-$BUILD-agent --region eu-central-1

echo "**delete master"
ec2_id=$(aws ec2 describe-instances --filter Name=tag:Name,Values=$CLUSTER_NAME-$BUILD-master --region eu-central-1 --query 'Reservations[*].Instances[0].InstanceId' --output text --region eu-central-1)
aws ec2 terminate-instances --instance-ids $ec2_id --output json --region eu-central-1