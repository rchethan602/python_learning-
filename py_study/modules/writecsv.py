import csv
req_file="/home/chethan/py_study/modules/demo_create.csv"

fo=open(req_file,'w')
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['sl_no', 'name', 'salary', 'skill'])
csv_writer.writerow(['1', 'chethan', '2000$'])
fo.close()
