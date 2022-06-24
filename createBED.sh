#!/bin/bash

# Use this script to convert the QAseq ref fasta coordinates to bed format

ref=$1
base=`basename ${sample} .fasta`

out=${ref/.fasta/.bed}
i=1
while IFS= read -r line; do
  if ((i % 2 == 1))
  then
    plexID=`echo $line | cut -c 2-`
    echo -ne "${plexID}\t0\t" 
  else
    echo ${#line}
  fi
  ((i++))
done <${ref}>${out}
