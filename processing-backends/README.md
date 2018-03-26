processing backends
===================
Subfolders here represent working `ansible projects` for 
bootstrapping processing backends. Only minor settings within the cloud-provider's 
web-consoles like ssh key-gen, IAM-policies, bucket-permissions 
are required beforehand.

## configuration overview

|        feature               | AWS | OTC |
| -----------------------------|:---:|:---:|
| structured VM Image gen      |  x  |  x  |
| VPC & subnets from scratch   |  x  |  x  |
| network sec-groups           |  x  |  x  |
| public https dashboards      |  x  |  x  |
| agent/worker autoscaling     |  x  |  x  |
| fine grained RoleBasedAccess |  x  |     |
| credential-less S3 comm      |  x  |     |
| preconfigured spark/alluxio  |  x  |  x  |
| multi-master setup           |     |     |
| elk stack for container logs |  x  |  x  |

##  what you get
- mesos cluster with one master (multi-master HA setup coming soon) and private agents within an autoscaling group (private IPs)
- distributed alluxio inMemory-FS accross mesos-agents (useable via alluxio-proxy REST API at `localhost:39999` on every cluster-node)
- alluxio underFS configured for S3
- readonly ssl enabled webUI & dashboards of `mesos` and `alluxio`
- cached nginx proxy for otc-instance metadata endpoints accessible at every node at  `localhost/user-data`
- elasticsearch/filebeat watching all agent container logs

![alt text](../img/whatyouget.png "whatyouget")

## why you want this
- for running batch-processing workloads on mesos from and to S3 optionally using an InMemory cache for intermediate data or results
- doing batch or distributed processing using `fast` InMemory-data with mesos-frameworks like `spark`, `storm` or `mesos-batch`
- to run analytics on selected and optionally cached datasets from S3
- monitor container logs and create custom metrics/dashboards