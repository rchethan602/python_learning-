import os
'''
import platform

OS=platform.system()

if OS == 'Linux':
    print(os.system('clear'))
else:
    print(os.system('cls'))
'''
path=input("Enter your path: ")

if os.path.exists(path):
    if os.path.isdir(path):
        print(f"Given {path} is directory")
    else:
        print(f"Given {path} is a file")
else:
    print(f"given {path} doesn't exists")
