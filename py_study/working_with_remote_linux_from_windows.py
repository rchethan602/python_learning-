#!/bin/python
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname='3.92.79.119',username='ec2-user',password='paramiko123',port=22)
ssh.connect(hostname='192.168.122.6',username='chethan',key_filename='/home/chethan/.ssh/id_rsa',port=22)
stdin, stdout1, stderr = ssh.exec_command('whoami')
stdin, stdout2, stderr = ssh.exec_command('uptime')
stdin, stdout3, stderr = ssh.exec_command('free -m')
print("The output is: ")
print(stdout1.read())
print(stdout2.read())
print(stdout3.read())

print("THe error is: ")
print(stderr.readlines())
