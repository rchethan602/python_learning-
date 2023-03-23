import subprocess
cmd="ls -lrt"


sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
#print(sp.communicate())
out,err=sp.communicate()

print(out)
print(err)


'''
cmd="env".split()
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(out)

'''
