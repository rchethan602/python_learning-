class date:
    def __init__(sf,dd=8 ,mm=6,yy=2022):
        sf.dd, sf.mm, sf.yy = dd,mm,yy
    def display(sf):
        print(sf.dd, sf.mm, sf.yy)
    def __str__(sf):
        return(str(sf.dd)+"/"+str(sf.mm)+"/"+str(sf.yy))
    def __add__(sf,days):
        #return(str(sf.dd)+"/"+str(sf.mm)+"/"+str(sf.yy))
         temp=date()
         temp.dd,temp.mm,temp.yy=sf.dd,sf.mm,sf.yy
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
             if temp.dd ==29 or temp.dd ==30 or temp.dd ==31:
                return temp

         return temp

today=date()
#today.display()
tomorrow=today+53
#tomorrow=today+1
#print(tomorrow)
tomorrow.display()
#today.display()
#print(tomorrow)
