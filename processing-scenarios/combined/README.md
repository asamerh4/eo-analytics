combined
=========

bundle batch processing-frameworks, git-control layer & jenkins...

first things first:
- cluster infos
  - monitoring of all VM's (low level) -> nagios (OS-layer)
  - live logs of master & agent processes -> elk (filebeat)
  - live logs of each container -> elk (filebeat of (mesos)container logs)

- data infos
  - use s3api to query data on s3 - create object indexes - ingest to elk - query using elk ~

- workflow infos
  - create pipeline dashboards based on realtime container logs

