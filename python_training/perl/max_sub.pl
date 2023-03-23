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
$max=max("Sun","Mon","Tue","Wed","Thu","Fri","Sat");
print $max,"\n"
