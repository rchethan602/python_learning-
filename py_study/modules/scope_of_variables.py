def myfunction1():
    x=60
    print("welcome to functions")
    print("x value from func1: ", x)
    myfunction2()
    return None

def myfunction2():
    print("Thank you")
    print("x value from func2: ", x)
    return None

def main():
    #x=10  , this x value cannot be used in myfunction2
    global x
    x=10
    myfunction1()
    return None

main()
