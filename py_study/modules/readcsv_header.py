import csv
req_file1="/home/chethan/py_study/modules/info.csv"

fo=open(req_file1, 'r')
content=csv.reader(fo)
#list1=list(content)
#print(f"The header is:\n {list1[0]}")
header=next(content)
print(header)
for each in content:
    print(each)
fo.close()
