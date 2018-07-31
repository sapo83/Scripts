#!/usr/bin/perl

### subroutine - calculate standard deviation of array
### argument - array of numeric values

sub calc_std_dev {
  my $n = @_;     ### number of values in array
  my $sum = 0;     ### set sum to 0
  foreach (@_)
    {
      $sum += $_;     ### calculate total sum of array
    }
  my $avg = $sum/$n;     ### calculate avg
  my $var_sum = 0;
  foreach (@_)
    {
      $var_sum += (($_ - $avg) * ($_ - $avg));     ### calculate top of var eq
    }
  my $var = ($var_sum / ($n - 1));     ### calculate variance
  my $std_dev = sqrt($var);     ### calculate standard deviation

  return $var;
}
