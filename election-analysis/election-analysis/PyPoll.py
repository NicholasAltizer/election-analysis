# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")

# Open the election results and read the file.
    #election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

### To do: perform analysis.
##    print(election_data)

### To do: read and analyze the data here.
## Read the file object with the reader function
    file_reader = csv.reader(election_data)

### Print each row in the CSV file
## for row in file_reader:
##    print(row)

# Read and print the header row.
headers = next(file_reader)
print(headers)

#close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

### Using the open() function with the "w" mode we will wrate data to the file.
## outfile = open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    ### Write some data to the file.
    ## txt_file.write("Hello World")

    ### Write three counties to the file.
    ## txt_file.write("Arapahoe, ")
    ## txt_file.write("Denver, ")
    ## txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


### Write some data to the file.
## outfile.write("Hello World")

### Close the file
## outfile.close()

# The data we need to retrieve
# 1. The total number of votes casted
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on popular vote.