import re
'''
text="This is pythonnnn and pythongnn"
my_pat=r'\bpython{4}\b'
print(re.findall(my_pat, text))

'''

'''
text="xaz asdfa sdf xaazz xaaaaaaaaaz xaaaaz"
#my_pat=r"\bxa{1,4}z\b"
#xa+z, a 1 or more times
#xa*z, 0 or more times
#xa?z 1 time or nonw
#xa{1,}z{1,2} , a one or more time and z 1 or 2 times
my_pat=r"\bxa{1,}z{1,2}\b"
print(re.findall(my_pat, text))
'''

#flags with regexp

text="This is a string THIS is a new string this"
my_pat=r"this"
print(re.findall(my_pat,text))
