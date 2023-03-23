$x=10;
$y=\$x;  #address
print $y,"\n";
print $$y, "\n";

@pens=('Parker','Cross','Sheaffer');
$arr=\@pens;
print $arr,"\n";
print("@$arr\n");
print("$$arr[0]\n");
print("$$arr[1]\n");
print("$$arr[2]\n");
print("$$arr[3]\n");
print("$$arr[-1]\n");
print("$$arr[-2]\n");
print("$$arr[-3]\n");
$len=@$arr;
print("length is $len\n");
print("Index of the last element is ", $#$arr, "\n");


%scores=("sachin",102,"sehwag",82,"kapil",90);
$hash=\%scores;
print($hash,"\n");
print("Score of sachin is $$hash{'sachin'}\n");
print("Score of sehwag is $$hash{'sehwag'}\n");
print("Score of kapil is $$hash{'kapil'}\n");

sub max {
  my $max;
  foreach $day(@_){
    print $day,"\n";
    if ($max lt $day) {
      $max = $day;
    }
  }
  return $max
}
$fun=\&max;
$ret=&$fun("Sun","Mon","Tue","Wed","Thu","Fri","Sat");
print ($ret);

@MDarray=(\$x,\@pens, \%scores, \&max);
print(${$MDarray[0]},"\n");
print(@{$MDarray[1][0]},"\n");
print(@{$MDarray[1][0]},"\n");
print(@{$MDarray[1][0]},"\n");
print(%{$MDarray[2]},"\n");
print(&{$MDarray[3]},"\n");
