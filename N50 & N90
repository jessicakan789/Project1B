# Set working Directory
getwd()
setwd("C:/Users/jadea/Documents/Msc Bioinformatics/Project 1B")
workingDir = "."
getwd()

# Import packages
library(Bios2cor)
library(Biostrings)

# Reading in Fasta assembly
assembly = import.fasta("assembly.fasta", aa.to.upper = TRUE, gap.to.dash = TRUE, log.file = NULL)

#reads the FASTA format and converts it into a manageable table of width, seq and names.
Septo = readDNAStringSet("assembly.fasta")

#Checking to see what the output is. 
print(Septo)

# see number of contigs, and the width (number of base pairs) for each contig
length(Septo)  # number of contigs
width(Septo)  # creates a vector with the width/length of each contig

#Frequency of bases 
alphabetFrequency(Septo,baseOnly=TRUE) #per contig
sum(alphabetFrequency(Septo, baseOnly=TRUE)) #Total number of nucleotides in the genome. 

#Frequency of bases as a %
alphabetFrequency(Septo,baseOnly=TRUE, as.prob = TRUE) #per contig
alphabetFrequency(Septo[[1]],baseOnly=TRUE, as.prob = TRUE) #per specified contig

#Total genome size
sum(width(Septo))

# Storing contig lengths as a vector. 
c_lengths = width(Septo)
total = sum(c_lengths)

#Creating a cumulative sum
c_sum = cumsum(c_lengths)
plot(c_sum) + abline(a = total/2, b = 0)

### Calculating the N50 (weighted median).
#The N50 contig size of an assembly (aka the N50 value) is the size of the largest contig such that the contigs larger than that have at least 50% the bases of the assembly.
N50(c_lengths) #227877

## Alternative way of calculating N50
len.sorted = rev(sort(c_lengths))
N50 <- len.sorted[cumsum(len.sorted) >= sum(len.sorted)*0.5][1]
print(N50) #227877

## Calculating N90 - the minimum contig length to cover 90 percent of the genome.
N90 = len.sorted[cumsum(len.sorted) >= sum(len.sorted)*0.9][1]
print(N90) #67860
