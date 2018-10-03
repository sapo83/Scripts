#!/usr/bin/perl
use strict;
use Bio::SeqIO;

### command line - perl get.seq.length.pl fasta_file
### output - sequence id & sequence length, tab separated

my $inputFasta = @ARGV[0];
#my $index;

my $inseq  = Bio::SeqIO->new(-file => "$inputFasta", -format => "fasta");

while(my $seq = $inseq->next_seq)
  {
    print $seq->display_id,"\t",$seq->length,"\n";
  }
