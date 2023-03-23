import os
import sys
from datetime import datetime
req_path=input("Enter the path: ")
req_old=eval(input("How many old days files you require: "))
if not os.path.exists(req_path):
    print("Provide valid path")
    sys.exit()
if os.path.isfile(req_path):
    print("Given path is file, not directory")
    sys.exit()

for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    if os.path.isfile(each_file_path):
        file_create_date=datetime.fromtimestamp(os.path.getctime(each_file_path))
        diff_days=(datetime.now()- file_create_date).days
        if diff_days < req_old:
            print(each_file_path,diff_days)
