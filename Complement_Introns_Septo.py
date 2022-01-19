# Count nucleotides and amino acids

from collections import Counter

Seq_list = ["Seq"]
Nuc_list = ["Nuc"]
Amino_list = ["Amino"]

# Create function that counts nucleotides

def display(index, counter):
    Nucs = 0
    for nucleotide in 'ACGT':
        Nucs += (counter[nucleotide])
    
    Amino = Nucs/3
    
    Seq_list.append(index)
    Nuc_list.append(Nucs)
    Amino_list.append(Amino)

    
# Turn file into string (get rid of white space) -> use above function
    
with open('assembly.fasta') as file:
    index = 0
    counter = Counter()

    for line in file:
        string = line.rstrip('\n')

        if string.startswith('>'):

            if index > 0:
                display(index, counter)

            index += 1
            counter.clear()
        else:
            counter.update(string)

    if counter:  
        display(index, counter)
        
        


# Tabulate using zip

tableData = [Seq_list, Nuc_list, Amino_list]

for row in zip(*tableData):
     print ('{:<10}{:>7}    {:<10}'.format(*row))

        



        
# 331 genes in total: 157 Coding, 169 Complement, 5 Introns

import re

f = open("Septobasidium.gbk", "r")

Lines = f.readlines()

Genes = 0

# Get all of the genes and print out how many nucleotides/amino acids per line

for line in Lines:
     if line.startswith("     gene"):
         Genes += 1

Complement = 0
Introns = 0

for line in Lines:
      x = re.search("gene            complement", line) 
      if x != None:
          Complement += 1
      y = re.search("mRNA            join", line) 
      if y != None:
          Introns += 1  
        
Coding = Genes - Complement - Introns       

print("\n Coding: ", Coding)
print("\n Complement: ", Complement)
print("\n Introns: ", Introns)
print("\n Total genes: ", Genes)
