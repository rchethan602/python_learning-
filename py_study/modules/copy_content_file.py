fo=open("random.txt",'r')
data=fo.read()
fo.close()

fo=open("/home/chethan/random1.txt",'w')
fo.write(data)
fo.close()
