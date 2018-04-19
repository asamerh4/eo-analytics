import boto.ec2
import uuid, os, sys

def is_true(x):
  return (x == True) or (x == 'True')

def append_uuid(x):
  return x + str(uuid.uuid4())

def vm_name(ip):
  from novaclient import client as novaclient

  creds = {}
  creds['username'] = os.getenv("OS_USERNAME")
  creds['api_key'] = os.getenv("OS_PASSWORD")
  creds['auth_url'] = os.getenv("OS_AUTH_URL")
  creds['project_id'] = os.getenv("OS_TENANT_NAME")

  nova = novaclient.Client("2", **creds)
  servers = nova.servers.list()

  s = filter(lambda s: (s.networks.get(creds['project_id'])[0] == ip), servers)[0]
  return s.name


def to_zookeeper_cluster_string(args):
  return (":" + str(args[1]) + ",").join(args[0]) + (":" + str(args[1]))

def private_zk_nodes(aws_region, cluster_id, access_key, secret_access_key):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.state == "running"):
        if i.tags.get("Name") == cluster_id+"-master":
          ips.append(i.private_ip_address)
  return ips

def public_zk_nodes(aws_region, cluster_id, access_key, secret_access_key):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.state == "running"):
        if i.tags.get("Name") == cluster_id+"-master":
          ips.append(i.ip_address)
  return ips

def mesos_master_nodes(aws_region, cluster_id, access_key, secret_access_key):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.state == "running"):
        if i.tags.get("Name") == cluster_id+"-master":
          ips.append(i.ip_address)
  return ips

def template_node(aws_region, cluster_id, access_key, secret_access_key):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.state == "running"):
        if i.tags.get("Name") == 'template':
          ips.append(i.ip_address)
  return ips

def control_node(aws_region, cluster_id, access_key, secret_access_key):
  ips = []
  conn = boto.ec2.connect_to_region(aws_region, aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

  for r in conn.get_all_reservations():
    for i in r.instances:
      if (i.state == "running"):
        if i.tags.get("Name") == 'control':
          ips.append(i.ip_address)
  return ips

class FilterModule(object):
    ''' Ansible UUID jinja2 filters '''

    def filters(self):
      return {
        'append_uuid': append_uuid,
        'vm_name': vm_name,
        'to_zookeeper_cluster_string': to_zookeeper_cluster_string,
        'private_zk_nodes': private_zk_nodes,
        'public_zk_nodes': public_zk_nodes,
        'mesos_master_nodes': mesos_master_nodes,
		'template_node': template_node,
        'control_node': control_node,
      }
