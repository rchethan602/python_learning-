#working with text files
'''
fo=open('newdemo.txt','w')
print(fo.mode)
print(fo.readable())
print(fo.writable())

'''

'''
import os
listp=['a','b','c','d']
fo=open("random.txt",'w')
for each in listp:
    fo.write(each+"\n")
fo.close()

'''
'''
listp=['aa','ba','cc','dd']
fo=open("random.txt",'a')
for each in listp:
    fo.write(each+"\n")
fo.close

'''
'''
fo=open("random.txt",'r')
data=fo.read()
fo.close
print(data)
'''
fo=open("random.txt",'r')
data=fo.readlines()
fo.close
print(data)
for each in range(3):
    print(data[each])
