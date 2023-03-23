import os

SRC=input("Enter the source file : ")
DST=input("Enter the New file: ")
data=open(SRC)
newfile=open(DST,"w")
'''
ctr=0
for line in data.readlines() :
    newfile.write(line)
data.close()
newfile.close()
'''
lines=data.readlines()
newfile.writelines(lines)

data.close()
newfile.close()
