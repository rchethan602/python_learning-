import os
import getpass
print(os.sep)
PWD=os.getcwd()
print(PWD)
os.chdir("/home/chethan")
PWD=os.getcwd()
print(PWD)
#print(os.listdir())
#os.mkdir("/home/chethan/pytest")
#os.rename("/home/chethan/pytest","/home/chethan/pytest1")
#print(os.environ)
print(os.getuid())
print(os.getgid())
print(getpass.getuser())
print(os.getpid())
