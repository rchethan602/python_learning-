
num1=2
while num1 <= 100 :
  num2=2
  while num2 <= num1/2 :
      if (num1 % num2) == 0 :
        break
      num2+=1
  else :
    print(num1)
  num1+=1
