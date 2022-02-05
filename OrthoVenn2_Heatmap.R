# Load packages
library(dplyr) # select() filter() 
library(lattice) # levelplot()
library(RColorBrewer) # display.brewer.all(colorblindFriendly=TRUE)
library(purrr) # reduce()

# Set working directory
setwd("C:/Users/jessica/OneDrive - University of Bath/Bioinformatics/Project 1B/OrthoVenn2")

# Get data
Septo <- read.csv("Septo_bio_process_file.txt", sep="\t", header=FALSE)
Botr <- read.csv("Botr_Septo_bio_process_file.txt", sep="\t", header=FALSE)
Ento <- read.csv("Ento_Septo_bio_process_file.txt", sep="\t", header=FALSE)
Pucc <- read.csv("Pucc_Septo_bio_process_file.txt", sep="\t", header=FALSE)
Sacc <- read.csv("Sacc_Septo_bio_process_file.txt", sep="\t", header=FALSE)

# Subset data
Septo_filter <- Septo[,2:3]
Botr_filter <- Botr[,2:3]
Ento_filter <- Ento[,2:3]
Pucc_filter <- Pucc[,2:3]
Sacc_filter <- Sacc[,2:3]

# Create list of data frames
All_filter <- list(Septo_filter, Botr_filter, Ento_filter, Pucc_filter, Sacc_filter)

# Merge into 1 table by full outer join
merged <- All_filter %>% reduce(full_join, by = "V2")
merged_table <- merged #copy table
names(merged_table)<-paste(list("description", "Septo", "Botr", "Ento", "Pucc", "Sacc")) # change column names

# change row names
row.names(merged_table) <- merged_table$description

# remove description column
merged_table$description <- NULL

# create heatmap
coul <- colorRampPalette(brewer.pal(8, "YlOrRd"))(25) # choose colours
merged_table_matrix <- as.matrix(merged_table) # convert from data frame to matrix
ckey <- list(labels=list(cex=0.5), height=0.5, width=1) #define size of colour key and text
png(filename = "OrthoVenn Heatmap.png",
    width = 800, height = 2080, units="px", res=300)
levelplot(t(merged_table_matrix), 
          col.regions = coul, 
          xlab="",
          ylab="", 
          aspect=10,
          scales=list(x=list(cex=0.5, rot=90),y=list(cex=0.2)),
          colorkey=ckey
) 
dev.off()
