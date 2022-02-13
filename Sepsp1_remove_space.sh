# https://stackoverflow.com/questions/15857088/remove-line-breaks-in-a-fasta-file

awk '!/^>/ { printf "%s", $0; n = "\n" } 
/^>/ { print n $0; n = "" }
END { printf "%s", n }
' Sepsp_Proteins.fasta > Sepsp1.fasta
