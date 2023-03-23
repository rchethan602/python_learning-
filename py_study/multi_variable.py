#!/usr/bin/python
x=3
y=5.7
lang_name="python_scripting"

#print("{} hello \n{} \n{}".format(y,x,lang_name))
my_output='{} hello \n{} \n{}'
#my_output=f"x value is: {x} \n the y value is: {y} \nthe lang_name is: {lang_name}"
print(my_output.format(y,x,lang_name))
