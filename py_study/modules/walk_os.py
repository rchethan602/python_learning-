import os
import sys
sys.exit()

path="/home/chethan"
#print(list(os.walk(path)))

for r,d,f in os.walk(path):
    if len(f)!=0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
print("=====================================")
