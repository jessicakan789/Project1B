# Create empty list
GO_ID = []

# Open GOE file
with open("./Plant/PLANT_GOE_file.txt") as file:
    lines = file.readlines()
    for line in lines: # read line by line
        GO_ID.append(line[0:10]) # append list

# Check GO_ID list
print(GO_ID)




# Using GO_ID from GOE, create list of contigs from cluster file
# Create empty list
Contigs = []
Contigs2 = []
Contigs3 = []

# Loop through cluster file
with open("./Plant/PLANT_cluster_file.txt") as file:
    lines = file.readlines()
    for ID in GO_ID: # Go through each ID
        for line in lines: # read line by line
            if ID in line:
                Contigs.append(line) # append list
                
# get rid of \n 
for item in Contigs:
    x = item.replace('\n', '')
    Contigs2.append(x)
                
# split string in contigs
for item in Contigs2:
    x = item.split('\t')
    Contigs3.append(x)
    
# Check Contigs list
print(Contigs3)




# Write out to csv
import csv

# field names 
fields = ["cluster_name", "protein_number", "swiss_prot_id", "go_annotation", "protein_list"] 
    
with open('PLANT_contigs.csv', 'w', newline='') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(Contigs3)
