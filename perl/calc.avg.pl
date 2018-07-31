#!/usr/bin/perl

### subroutine - calculates average
### argument: array of numeric values

sub calc_avg {
  my $n = @_;     ### number of values in array
  my $sum = 0;     ### set sum to 0
  foreach (@_)
    {
      $sum += $_;     ### calculate total sum of array
    }
  my $avg = $sum/$n;     ### divide total sum of array by the numebr of values in array
  return $avg;
}
