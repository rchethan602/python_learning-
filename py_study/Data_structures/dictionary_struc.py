
my_dict={}
print(my_dict,type(my_dict))
print(bool(my_dict))
'''
my_dict={'fruit':'apple','animal':'fox','tree':'coconut',1:'one','two':2}
'''
#print((my_dict))
#print(my_dict['fruit'])
#print(my_dict.get('animal'))
#print(my_dict['three'])
#print(my_dict.get('three'))
#my_dict.clear()
'''
print(my_dict)
my_dict['three']=3
print(my_dict)
my_dict['three']=56
print(my_dict)
'''
print(my_dict)
'''
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
y=my_dict.copy()
print(id(y),id(my_dict))
'''

'''
my_new_dict={'four':4}
my_dict.update(my_new_dict)
print(my_dict)
my_dict.pop('four')
print(my_dict)
removed_item=my_dict.popitem()
print(my_dict)
print(removed_item)
'''
'''
keys=['a','e','i','o','u']
new_dict=dict.fromkeys(keys)
print(new_dict)
new_dict['a']=1
print(new_dict.get('a'))
'''