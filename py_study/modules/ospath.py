import os
path1="/home/chethan/py_study"
print(os.path.basename(path1))
print(os.path.dirname(path1))
path2="modules"
print(os.path.join(path1,path2))
path3=os.path.join(path1,path2)
print(os.path.split(path3))
print(os.path.getsize("/home/chethan"))
print(os.path.exists(path1))
os.path.isfile(path1)
os.path.isdir(path1)
print(os.path.islink("/usr/bin/python"))
