#!/bin/bash

sudo yum -y install gcc python-devel
sudo pip install pip --upgrade
sudo pip install markupsafe --upgrade
sudo pip install apache-airflow cryptography
sudo chown -R centos:centos /home/centos/airflow
echo ""
echo "1) run airflow initdb"
echo "2) run airflow webserver"
echo "3) place dags in /home/centos/airflow/dags"
echo "4) goto https://PUBLIC-IP/airflow"