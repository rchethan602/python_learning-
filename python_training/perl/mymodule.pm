package MyModule;
use carp;
require Exporter;
@ISA = qw/Exporter;
@EXPORT=qw/function;

sub function{
  carp "Error in My module";
}
1;
