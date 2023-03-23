#NameError
#TypeError
#FileNotFoundError
#ZeroDivisionError

#Nameerror
#a=3
try:
    print(a) #NameError
#    print(4+"string") #TypeError
    #open('assbdj.txt') #FileNotFoundError
except NameError:
    print("variable not defined")
except TypeError:
    print("adding number and string is not possible")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
else:
    print("This will execute if there is no exceptions in try block")

'''
finally:
    print("this is finally what gets executed irrespective of exceptions handled, even if the try block is success")

'''
# user defined exceptions
'''
age=23

if age>23:
    print("valid age")
else:
    raise ValueError("age is greater than 30")
'''
age=30

try:
    assert age<30
except AssertionError:
    print("Raised with assert because age is lessthan 30")
except:
    print("Exception occured")
