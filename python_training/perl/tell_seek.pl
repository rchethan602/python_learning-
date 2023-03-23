#!/usr/bin/perl
print "Enter your Filename: ";
$file = <STDIN>;
open FH,"<$file";
$line=<FH>;
$te= tell FH;
while($line){
  print $line;
  seek FH, $te, 0;
  #$line=<FH>;
  $line=<FH>;
  print $line;
  $te= tell FH;
}

close FH;
