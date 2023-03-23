num_word={1:'one',2:'two',3:'three',4:'four'}
num=eval(input("Enter a number: "))

if num in num_word:
    print(num_word.get(num))
else:
    print("number is out of range")
