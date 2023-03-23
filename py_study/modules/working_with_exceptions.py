'''
print("welcome to exceptions concept")

print("Now it is fine")
#print(4/0)
try:
    fo=open("nari.txt")
    print(fo.read())
    fo.close()
except Exception as e:
    print("could be file not found")
    print(f"This is because of {e}")

#print("proceeding")
'''
try:
    print(my_list[4])
except Exception as e:
    print(e)
