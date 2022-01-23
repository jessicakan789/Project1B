from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import GC

#reporting GC content as a percentage for each contig.
for seq_record in SeqIO.parse(r"C:\\Users\\jadea\Documents\\Msc Bioinformatics\\Project 1B\\Septobasidium\\assembly.fasta", "fasta"):
    print(GC(seq_record.seq))
