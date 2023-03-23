'''
my_str="Python Scrpting"
print(my_str.startswith('P'))
print(my_str.endswith('hon'))
print(my_str.islower())
print(my_str.istitle())
print(my_str.isspace())#  false  - is space to check entire string
my_new_str=" "
print(my_new_str.isspace()) #  true , dclared value is space
print(my_str.isalpha())
'''

'''
print(my_str.strip())

#x=" ermc "
#print(x.strip()) #strip will remove starting or ending side of char mentioned in strip
y="pythonp"
print(y.strip('p'))
print(y.lstrip('p'))
print(y.rstrip('p'))
'''

'''
my_sentence="strip is will remove starting or ending side of is char mentioned in strip"
print(my_sentence.split('is'))
'''
my_sentence="strip is will remove starting or ending side of is char mentioned in strip"
print(my_sentence.count('strip')) #counts number of repeats
print(my_sentence.index('is')) #finds index of 1st letter
my_sentence_split=my_sentence.split()
print(my_sentence_split)
print(my_sentence_split.index('will'))
print(my_sentence.find('z'))
print(my_sentence.find('s'))
