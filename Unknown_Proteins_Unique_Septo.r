# Set working Directory
getwd()
setwd("C:/Users/jadea/Documents/Msc Bioinformatics/Project 1B")
workingDir = "."
getwd()

# Load libraries
library(ggplot2)
library(dplyr)
library(lattice)
library(RColorBrewer)

options(stringsAsFactors = FALSE)

# Read in PLANT_analysis excel sheet
my_data <- read.table(file = "clipboard", 
                      sep = "\t", header=FALSE)

# View data as a table.
View(my_data)

# Adding headings to the table 
colnames(my_data) = c("Cluster_name", "protein_number", "swiss_prot_id", "go_annotation", "protein_list")

# View data as a table.
View(my_data)

# Removing "Septobasidium cavarae" from table 
my_data$protein_list = gsub("Septobasidium_cavarae|", "", as.character(my_data$protein_list))

# View data as a table.
View(my_data)

# Setting cluster number as row names
row.names(my_data) = my_data$Cluster_name
my_data$Cluster_name = NULL

# Unknown proteins
Unknown_Septo_Plant = filter(my_data, swiss_prot_id == "N/A")
View(Unknown_Septo_Plant)

# Save Unknown Proteins file
write.csv(Unknown_Septo_Plant, file = "Unique_Unknown_Septo_Proteins.txt")
