import os

FILE=input("Enter your Filename : ")
data=open(FILE)
ctr=0
for line in data.readlines() :
    ctr+=1
    print(ctr , line, end="")
data.close()

'''
ctr=0
line=data.readline()
while line :
    ctr+=1
    print(ctr,line)
    line=data.readline()
data.close()
'''
