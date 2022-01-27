# Create empty list
amino_acids = []

# Open amino acid file
with open("Septo_prot.aa.fasta") as file:
    for line in file: # read line by line
        if not line.startswith(">"): # exclude headers
            amino_acids += line # append list
            
# Create another empty list
amino_acids_count = 0
for i in amino_acids:
    amino_acids_count += len(i)
    
print(amino_acids_count)
