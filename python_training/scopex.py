#!/usr/bin/python
a, b, c, d = 10, 20, 30, 40
def funA():
    a, b, c=100, 200, 300
    print("In fun A", a, b, c, d)
    def funB():
        a, b=1000, 2000
        print("In fun B", a, b, c, d)
        def funC():
            a=10000
            print("In fun C", a, b, c, d)
        funC()
    funB()
funA()
print("In __main__",a,b,c,d)
