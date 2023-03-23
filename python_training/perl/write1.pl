open RFH, "<files.pl";
open WFH, ">writefile1";
while(<RFH>){
  print $_;
  print WFH $_;
}
