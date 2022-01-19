# Alternative method

from collections import Counter

Seq_list = ["Seq"]
Nuc_list = ["Nuc"]
Amino_list = ["Amino"]
Partial_list = ["Partial codon"]

# Create function that counts nucleotides

def display(index, counter):
    print("Sequence {}:".format(index))
    
    Nucs = 0
    for nucleotide in 'ACGT':
        Nucs += (counter[nucleotide])
    
    Amino = Nucs/3
    
    #Doesn't work - supposed to identify partial codons
    if Amino%3 != 0:
        Partial = "Yes"
    else:
        Partial = "No"
    
    print('Nucs: ', Nucs)
    print('Amino: ', Amino)
    print("\n")
    
    Seq_list.append(index)
    Nuc_list.append(Nucs)
    Amino_list.append(Amino)
    Partial_list.append(Partial)

    
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
        
        
        
print(Seq_list)
print(Nuc_list)
print(Amino_list)   
print(Partial_list)

# Tabulate using zip

tableData = [Seq_list, Nuc_list, Amino_list, Partial_list]

for row in zip(*tableData):
     print ('{:<10}{:>7}    {:<10} {:<10}'.format(*row))

        
# Tabulate using pandas
        
import pandas as pd
pd.DataFrame(tableData).T


# Number of partial codons

Total_partial_codons = 0

for i in Partial_list:
    if i=="Yes":
        Total_partial_codons +=1

print("\n Partial: ", Total_partial_codons) 
