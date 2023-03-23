print "Enter your Filename: ";
$file = <STDIN>;
open FH,"<$file";
$line=<FH>;

while($line){
  if ($line =~ /^#/){
    $ctr=0;
  }else{

    print($line,"\n");
  }
  $line=<FH>;
}

while($line){
  if ($line !~ /^#/){
    $ctr=0;
  }else{

    print($line,"\n");
  }
  $line=<FH>;
}
