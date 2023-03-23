%sam=('maths',90,'English',83);
%tom=('maths',92,'English',87);
%jerry=('maths',90,'English',84);

%students=('sam',\%sam,'tom',\%tom,'jerry',\%jerry);

foreach $student (keys %students){
  foreach $subject (keys %$student){
    print ("$student scored $$student{$subject} in $subject \n");
  }
}

foreach $student (keys %students){
foreach $subject (keys %{$students{$student}}){
print("$student scored $students{$student}{$subject} in $subject \n");
}
}
