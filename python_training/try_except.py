ctr=1
while ctr != -1:
    try:
        ctr=int(input("Enter a number(-1 to exit): "))
    except ValueError:
        print("That was not a number")
    except:
        print("Default Exeption Handler")
    else:
        print("No exception found")
    finally:
        print("This executes always")
