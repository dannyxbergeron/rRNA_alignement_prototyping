#!/bin/bash

in_files=(
  "../data/raw_data_processed/18S_V5.fasta"
  "../data/raw_data_processed/28S_V5.fasta"
)
out_files=(
  "../data/raw_data_processed/18S_V5_aligned.fasta"
  "../data/raw_data_processed/28S_V5_aligned.fasta"
)

# Iterate over zipped in_files and out_files
for i in "${!in_files[@]}"; do
  in_file="${in_files[$i]}"
  out_file="${out_files[$i]}"
  clustalo \
    -i "$in_file" \
    -o "$out_file" \
    --outfmt=fasta \
    --force
done
