#!/usr/bin/perl

$x=10;
$name="India";
print("value of $x is $x \n");
$x=5;
print('value of $x is $x', "\n");
print(
"value of
\$x is $x","\n"
);
print($name,"\n");

@pens=('Parker','Cross','Sheaffer');
print("@pens\n");
print("@pens[0]\n");
print("@pens[1]\n");
print("@pens[2]\n");
print("@pens[3]\n");
print("@pens[-1]\n");
print("@pens[-2]\n");
print("@pens[-3]\n");
$len=@pens;
print("length is $len\n");
print ("Index of the last element is $#pens","\n");
%scores=("sachin",102,"sehwag",82,"kapil",90);
print($scores{'sachin'},"\n");
print("@pens[Parker]");
