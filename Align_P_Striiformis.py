# Create list of contigs and alignment

Contig_list = list(range(1, 283, 1))
Align_list = []

# Read line by line
    
with open('blastn_Puccinia_Striiformis.txt') as file:

    for line in file:
        
        if line.startswith('Sequences producing significant alignments'):
            Align_list += "1"
            
        elif line.startswith('***** No hits found *****'):
            Align_list += "0"

print(Contig_list)
print(Align_list)

# Tabulate using pandas
        
import pandas as pd

tableData = [Contig_list, Align_list]
Align = pd.DataFrame(tableData)
print(Align)

# Write out to csv

Align.to_csv(r'Align_P_Striiformis.csv')
