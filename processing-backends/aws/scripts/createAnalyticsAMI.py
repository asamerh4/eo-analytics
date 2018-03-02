import argparse
from subprocess import call

parser = argparse.ArgumentParser(description = 'create eo-analytics AMI')

parser.add_argument("region",
                    choices = ["eu-central-1"],
                    help = "The AWS region to run the image-building process")

parser.add_argument('cluster-id',
                    help = 'A unique identifier per OTC region for your Mesos cluster')

parser.add_argument("-k", "--ssh-key", dest = 'ssh-key', type = str,
                    help = "path to ssh-key (*.pem file)")

parser.add_argument("-ok", "--aws-ssh-key-name", dest = 'aws-ssh-key-name', type = str,
                    help = "name of keypair registered in AWS-IAM")

parser.add_argument("-u", "--remote-user", dest = 'remote-user', type = str,
                    help = "remote user for EC2 instance (sudo)")

parser.add_argument("-f", "--ansible-vault-password-file", dest = 'password_file',
                    help = "The location of the file containing the Ansible Vault password")

args = parser.parse_args()
arg_vars = vars(args)

#ansible_prompt = "--ask-vault-pass"
#if arg_vars["password_file"]:
#  ansible_prompt = "--vault-password-file={}".format(args.password_file)


call(["ansible-playbook",
          "--private-key={}".format(arg_vars["ssh-key"]),
		  
		  "-e", "remote_user={}".format(arg_vars["remote-user"]),
          "-e", "aws_ssh_key_name={}".format(arg_vars["aws-ssh-key-name"]),
          "-e", "cluster_id={}".format(arg_vars["cluster-id"]),
          "-i", ",",
          "tasks/machineImage.yml"])
