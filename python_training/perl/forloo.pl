#!/usr/bin/perl

for ($i=1; $i<=10; $i++){
  print($i,"\n");
  if($i==5){last};
  #or
  #last if($i==5);
}

@array=(0,1,2,3,4,5,6);
foreach $element (@array){
print($element,"\n");
}

%scores=("sachin",102,"sehwag",82,"kapil",90);
@keys=keys %scores;
print @keys,"\n"

%scores=("sachin",102,"sehwag",82,"kapil",90);
foreach $player (keys %scores) {
  print("$player");
}
