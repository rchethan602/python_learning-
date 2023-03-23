print "Enter your source Filename: ";
$src = <STDIN>;
print "Enter your dest Filename: ";
$dst = <STDIN>;
open FH,"<$src";
@lines=<FH>;
open WFH,">$dst";
print WFH "@lines";
