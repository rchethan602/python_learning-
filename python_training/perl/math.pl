#!/usr/bin/perl
$a=10;
$b=20;
print($a+$b,"\n");
print($a-$b,"\n");
print($a*$b,"\n");
print($a/$b,"\n");
print($a%$b,"\n");
print($a**3,"\n");

print ("*" x 30);
###
===
!=
<
<=
>
>=
###

string comparison operators
eq
ne
lt
le
gt
ge

assignment operators

=
+=
-=
/=
*=
**=
%=

logcial operators
and
or
not

. concatenation operators
x repetition operators  *x5= *****

++ --
###

if (condition) {
  set of statemtns
}elseif (condition){

}
else{

}

#opposite of IF
unless(condition){

}else{

}

#opposite to while loop
until(condition becomes true){

}

for loop

for(initialization; condition; incr/decr){
set of statements
}

@array=(0,1,2,3,4,5,6);
foreach $element (@array){
print($element,"\n");
}

Associative array,
Addition
$scores{"key"}=value;
delete
$scores{"key"}

breaking from loop
#or
#last if($i==5);


seek FH,position, whence
whence
  0 - BOF
  1 - Current file pointer position
  2 - EOF

tell FH
