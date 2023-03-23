import subprocess
cmd="bash --version".split()
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()

if rc==0:
    for each_line in out.splitlines():
        if "version" in each_line and "release" in each_line:
            index=each_line.split().index("version") + 1
            print(each_line.split()[3])
else:
    print("Wrong command")
