sub display{
  $ctr=0;
  ($n,$m)=@_; #which hold parametrs to function
  foreach (@$n){
    print($$n[$ctr]," ",$$m[$ctr],"\n");
    $ctr+=1;
  }
}
@names=('sam','tom','jerry');
@marks=(10,20,30);
display(\@names, \@marks);
