#!/usr/bin/perl

print "Enter your Filename: ";
$file = <STDIN>;
open FH,"<$file";
$line=<FH>;
$count=1;

while ($line){
  print("$count  $line");
  $line=<FH>;
  $count++;
}
