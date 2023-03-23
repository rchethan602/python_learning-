import os
req_file=input("Enter your filename to search: ")
req_path=input("Enter path where file needs to be search: ")

if os.path.exists(req_path):
    print(req_path)
    for r,d,f in os.walk(req_path):
        if len(f) != 0:
            for each_file in f:
                if each_file == req_file:
                    print(os.path.join(r,each_file))
else:
    print("given path doesn't exist")
