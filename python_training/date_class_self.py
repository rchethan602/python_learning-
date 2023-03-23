class date:
    def __init__(self,dd=8 ,mm=6,yy=2022):
        self.dd, self.mm, self.yy = dd,mm,yy
    def display(self):
        print(self.dd, self.mm, self.yy)
    def __str__(self):
        print("In __str__")
        return(str(self.dd)+"/"+str(self.mm)+"/"+str(self.yy))
    def __repr__(self):
        print("In __repr__")
        return(str(self.dd)+"/"+str(self.mm)+"/"+str(self.yy))
'''
    def __add__(self,days):
        #return(str(self.dd)+"/"+str(self.mm)+"/"+str(self.yy))
         temp=date()
         temp.dd,temp.mm,temp.yy=self.dd,self.mm,self.yy
         temp.dd+=days
         while temp.dd > 28:
             if temp.dd > 30 and temp.mm in (4,6,9,11):
                 temp.dd-=30
                 temp.mm+=1
             if temp.dd > 31 and temp.mm in (1,3,5,7,8,10,12):
                 temp.dd-=31
                 temp.mm+=1
                 if temp.mm == 13:
                      temp.mm=1
                      temp.yy+=1
             if temp.dd >= 28 and temp.mm ==2 and temp.yy % 4 !=0:
                 temp.dd-=28
                 temp.mm+=1
             if temp.dd > 29 and temp.mm ==2 and temp.yy % 4 ==0:
                 temp.dd-=29
                 temp.mm+=1
             else:
                 break

         return temp

'''
today=date()
#today.display()
print(str(today))
print(repr(today))
#tomorrow=today+1
#print(tomorrow)
#tomorrow.display()
#today.display()
#print(tomorrow)
