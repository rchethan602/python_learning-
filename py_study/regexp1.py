#findall ,

import re
text="This is a python2 _ and it is easy to _l learn _@ python34"
'''
my_pat="is\w"
print(re.findall(my_pat,text))
#print(len(re.findall(my_pat,text)))
#pattern i[st]
'''
#\w means atoz  or AtoZor 1to9 or underscore
#\w\w means 2 characers , combination of atoz  or AtoZ or 1to9 or underscore
#\W means it looks for charcaters that are not part of small \w

'''
my_pat="\w\w\w"
print(re.findall(my_pat,text))
'''
#my_pat="\d" to loof for string which contains digits
#\d,\d to look for string whcih contains 2 digits
#\. = dot to match only dots, if no slash it will match eveything including space
my_pat="python\d"
print(re.findall(my_pat,text))
