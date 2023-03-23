



DAY=input("Enter the day : ")
'''
DAY=var.lower()
workdays=["monday","tuesday","wednesday","thursday","friday"]
'''



if DAY == "monday"  or DAY == "tuesday" or  DAY == "wednesday"  or DAY == "thursday" or DAY == "friday"  :
    print("9:00AM to  5:30PM")
elif DAY=="saturday" :
    print("9:00AM to  1:00PM")
elif DAY=="sunday" :
    print("Its Holiday")
