#!/usr/bin/pythonn3

file=input("Enter the file name: ")
fobj=open(file)
loc=fobj.tell()
line=fobj.readline()
ctr=1
while line :
    print(ctr,line, end="")
    fobj.seek(loc)
    line=fobj.readline()
    print(ctr,line, end="")
    loc=fobj.tell()
    print(loc)
    line=fobj.readline()
    ctr+=1
