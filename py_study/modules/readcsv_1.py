import csv
'''
req_file1="/home/chethan/py_study/modules/info.csv"

fo=open(req_file1, 'r')
content=csv.reader(fo)
for each in content:
    if "name" not in each:
        print(each)
fo.close()
'''
req_file1="/home/chethan/py_study/modules/new_info.csv"

fo=open(req_file1, 'r')
content=csv.reader(fo,delimiter="|")
for each in content:
    if "name" not in each:
        print(each)
fo.close()
