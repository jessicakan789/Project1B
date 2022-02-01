#!/bin/bash

# Code modified from https://angus.readthedocs.io/en/2016/running-command-line-blast.html

# Get Cronartium quercuum FASTA genome
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/015/951/145/GCA_015951145.1_Croqu1/GCA_015951145.1_Croqu1_protein.faa.gz

# Rename file
mv GCA_011750755.1_ASM1175075v1_genomic.faa.gz C_quercuum.faa.gz

# Unzip
gunzip C_quercuum.faa.gz

# Create Database for BLASTp
makeblastdb -in C_quercuum.faa -dbtype prot

# BLASTp 
blastp -query Septo_prot.aa.fasta -db C_quercuum.faa -out blastp_C_quercuum.txt -outfmt 6
