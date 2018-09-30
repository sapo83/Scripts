#!/usr/bin/perl
use strict;
use Bio::DB::Fasta;

### command line - perl parse.fasta.pl list_of_IDs fasta_to_parse output_filename

my $IDlist = @ARGV[0];
my $inputFasta = @ARGV[1];
my $outputFasta = @ARGV[2];
my $index;

open IDFILE, $IDlist or die $!;    ### Open input ID list
open OUTPUT, $outputFasta or die $!;     ### open output fasta file

$index = Bio::DB::Fasta->new("$inputFasta") or die $!;

while (<IDFILE>)
  {
    my ($id) = (/^>*(\S+)/);
    my $header = $index->header($id);
    print OUTPUT  ">$header\n", $index->seq( $id ), "\n";
  }
