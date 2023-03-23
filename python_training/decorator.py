def divide(a,b):
    return a/b
def validated_divide(fun):
    def nested(x,y):
        if x < y : x,y=y,x
        return fun(x,y)
    return nested

print(divide(10,20))
divide=validated_divide(divide)
print(divide(10,20))


def gen2(n):
    ctr=1
    ctr=0
    lst=list(range(n))
    while True:
        if ctr==n:
           return
        ctr+=1
    yield lst[ctr]
        gn2=gen2(100)  gn2.__next__() 1  gn2.__next__() 2  gn2.__next__()
Send to:
