'''def get_result(x):
    result=0
    result=x+10
    print(f"your result is: {result}")
    return None

def main():
    #global num
    num=eval(input("Enter your number: "))
    get_result(num)
    return None

main()'''
'''
def get_addition(a,b):
    result=a + b
#    print(f"the result is: {result}")
    return result or return a+b
def main():
    a=eval(input("Enter value of first number: "))
    b=eval(input("Enter value of second number: "))
    result=get_addition(a,b)
    print(f"the result is: {result}")
    return None
main()

'''
#default argument

'''
def my_func(a,b=2):
    print(a,b)

my_func(3)

'''
#variable length arguments
#here data1 can be multiple values

'''
def length_var(*data1):
    for each in data1:
        print(each)

length_var(1,"hi",2+3j)


'''

#variable keyword based arguments

'''
def myfunction(**data):
    print(data)

myfunction(x=1,y=3)
myfunction(x=1,y=3,name="Chethan")
#o/p {'x': 1, 'y': 3}
'''

def mult(a,b)
    print(f"the mul is {a*b}")
    return None

x=7
y=4
