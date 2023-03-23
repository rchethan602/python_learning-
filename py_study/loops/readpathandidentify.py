import os
import sys
path=input("Enter directory path: ")

if os.path.exists(path):
    print(f"{path} exists")
    file_dirs=os.listdir(path)
    print(f"There are total {len(file_dirs)} objects")
    for i in file_dirs:
        fullp=os.path.join(path,i)
        if os.path.isfile(fullp):
            print(f"{fullp} is a file")
        else:
            print(f"{fullp} is directory")
else:
    print("path doesn't exist")
    sys.exit()

my_dict={'one':1,'two':2, 'three':3}
