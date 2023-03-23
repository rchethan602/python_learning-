import os

print(os.system("clear"))

RC=os.system("ls -ld .")
# no need to print it os.system will return the data to screen
if RC == 0:
    print("yes")
else:
    print("no")
