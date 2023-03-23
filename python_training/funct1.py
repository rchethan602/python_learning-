'''
def total(a=0,b=0, *c) :
    sum=a+b
    for value in c :
        print(value)
        sum=sum+value
    print(sum)

total(1,2,3,4,5)


def total(a=0,b=0, *c, **d) :
    sum=a+b
    for value in c :
        sum+=value
    for key in d.keys():
        sum+=d[key]
    print(sum)

total(1,2,3,4,5,p=300,q=200,100)
'''

def total(a=0,b=0, *args, **kwargs) :
    sum=a+b
    for value in args :
        sum+=value
    for key in kwargs.keys():
        sum+=kwargs[key]
    print(sum)
