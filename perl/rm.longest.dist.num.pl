#!/usr/bin/perl

### subroutine - finds the number farthest from the mean & removes it from the array
### arugment: an array of numeric values

sub find_longest_dist {
  my $n = @_;     ### number of values in array
  my $sum = 0;     ### set sum to 0
  foreach (@_)
    {
      $sum += $_;     ### calculate total sum of array
    }
  my $avg = $sum/$n;     ### calculate avg

  my @array = sort { $a <=> $b } @_;     ### sort array numerically
  my $min_dist = abs($array[0] - $avg);     ### find distance of minimum number
  my $max_dist = abs($array[-1] - $avg);     ### find distance of maximum number

  if ($min_dist > $max_dist)     ### remove value with highest distance
    {
      @array = @array = @array[ 1 .. $#array ];
    }
  else
    {
      pop @array;
    }
  return @array;
}
