#!/bin/bash

# Code modified from https://angus.readthedocs.io/en/2016/running-command-line-blast.html

# Get Puccinia Striiformis FASTA genome
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/011/750/755/GCA_011750755.1_ASM1175075v1/GCA_011750755.1_ASM1175075v1_genomic.fna.gz

# Rename file
mv GCA_011750755.1_ASM1175075v1_genomic.fna.gz Puccinia_Striiformis.fna.gz

# Unzip
gunzip Puccinia_Striiformis.fna.gz

# Create Database for BlastN
makeblastdb -in Puccinia_Striiformis.fna -dbtype nucl

# BlastN 
blastn -query assembly.fasta -db Puccinia_Striiformis.fna -out blastn_Puccinia_Striiformis.txt #-outfmt "6 qseqid sseqid slen qstart qend length mismatch gapopen gaps sseq" 

## In theory we should be able to add -outfmt to the end to get the txt file as a tabular format and after that we can specify what we want to be reported.
# However -outfmt isn't recognised in CLIMB on BLASTn even though it is listed when you blastn -help.

