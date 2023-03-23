$sentence="i dont sell sea shells on the sea shore";
if ($sentence =~ /shells/){
  print($sentence,"\n");
  print("$` \n");
  print("$& \n");
  print("$' \n");
}
$sentence="She sell sea shells on the sea shore";
$sentence=~ s/she/someone/ig;
print($sentence,"\n");

if ($sentence =~ /shells|other/){
  print($sentece,"\n");
}

#comment
#comment
#comment
