import os
import time
import platform

def my_func(cmd1,cmd2):
    print("Please enter command after 2 seconds")
    time.sleep(2)
    print("clearing the screen")
    os.system(cmd1)
    print("listing dirs")
    os.system(cmd2)

if platform.system() == "Windows":
    my_func("cls","dir")
if platform.system() == "Linux":
    my_func("clear","ls -lrt")
