#!/usr/bin/perl
print "Enter the day: ";
$day = <STDIN>;
chomp($day);
$day=lc($day);
#@workdays=("monday","tuesday","wednesday","thursday","friday");

if ($day eq "monday" or $day eq "tuesday" or $day eq "wednesday" or $day eq "thursday" or $day eq "friday" ) {
  print("Working time - 9 to 5:30 \n");
} elsif ($day eq "saturday") {
  print("Working time - 9 to 1 \n");
} elsif ($day eq "sunday") {
  print("Its Holiday \n");
}
