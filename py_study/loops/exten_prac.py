import os
import sys
req_path=input("Enter the path: ")
if os.path.exists(req_path):
    if os.path.isfile(req_path):
        print("given path is not directory")
        sys.exit()
    else:
        req_ext=input("Enter the extension of files you are looking for(.py/.sh/.bat): ")
        f_d=os.listdir(req_path)
        req_files=[]
        for eachf in f_d:
            if eachf.endswith(req_ext):
                req_files.append(eachf)
        if len(req_files)==0:
            print(f"path doesn't have any {req_ext} files")
            sys.exit()
        else:
            print(req_files, len(req_files))
else:
    print("Path doesn't exist")
