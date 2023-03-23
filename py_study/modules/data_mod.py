import datetime
print(datetime.datetime.now().strftime("%y-%m-%d%H:%M:%S"))
print(datetime.datetime.today())
#to get timezone we need to define it 1st using pytz
import pytz
ist=pytz.timezone('Asia/Kolkata')
print(datetime.datetime.now(ist)
from datetime import datetime

print(datetime.today())
