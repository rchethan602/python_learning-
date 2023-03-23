class UDException(Exception):
    pass

ctr=1
while ctr != -1:
    try:
        ctr=int(input("Enter a number (-1 to exit):"))
        if ctr == 5:
          raise UDException
    except UDException:
        print("That was user defined exception")
