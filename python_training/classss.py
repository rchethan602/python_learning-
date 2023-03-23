class Mom:
 def __del__(self):
  print("Object Destoryed")
 def Walk(self):
  print("Walk-Mom", id(self))

 def __init__(self):
  print("Object contructed successfully")

Mother=Mom()
Mother.Walk()
print("id of mother is", id(Mother))
del(Mother)
print("THis is the last print")
