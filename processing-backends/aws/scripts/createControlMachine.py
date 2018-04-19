###########
#IMPORTANT#
###########

#EXECUTE ONLY FROM YOUR PERSONAL LINUX HOST WHERE YOUR SECURE SSH-KEYS ARE STORED!

import argparse
from subprocess import call

parser = argparse.ArgumentParser(description = 'create control Machine')

parser.add_argument("region",
                    choices = ["eu-central-1"],
                    help = "The AWS region to run the image-building process")

parser.add_argument('cluster-id',
                    help = 'A unique identifier per OTC region for your Mesos cluster')

parser.add_argument("-k", "--ssh-key", dest = 'ssh-key', type = str,
                    help = "path to ssh-key (*.pem file)")

parser.add_argument("-ck", "--cluster-ssh-key", dest = 'cluster-ssh-key', type = str,
                    help = "path to cluster-ssh-key (*.pem file)")

parser.add_argument("-ok", "--aws-controlMachine-ssh-key-name", dest = 'aws-controlMachine-ssh-key-name', type = str,
                    help = "name of keypair registered in AWS-IAM")

parser.add_argument("-ock", "--aws-cluster-ssh-key-name", dest = 'aws-cluster-ssh-key-name', type = str,
                    help = "name of cluster keypair registered in AWS-IAM")

parser.add_argument("-u", "--remote-user", dest = 'remote-user', type = str,
                    help = "remote user for EC2 instance (sudo)")

parser.add_argument("-f", "--ansible-vault-password-file", dest = 'password_file',
                    help = "The location of the file containing the Ansible Vault password")

args = parser.parse_args()
arg_vars = vars(args)

call(["ansible-playbook",
          "--private-key={}".format(arg_vars["ssh-key"]),
		  "-e", "remote_user={}".format(arg_vars["remote-user"]),
          "-e", "aws_ssh_key_name={}".format(arg_vars["aws-cluster-ssh-key-name"]),
          "-e", "aws_controlMachine_ssh_key_name={}".format(arg_vars["aws-controlMachine-ssh-key-name"]),
          "-e", "aws_ssh_key_file={}".format(arg_vars["cluster-ssh-key"]),
          "-e", "cluster_id={}".format(arg_vars["cluster-id"]),
          "-i", ",",
          "tasks/controlMachine.yml"])
