# The data we need to retrieve.
#1. The total number of votes cast
#2. a complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load =os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
     # To do: read and analyze the data here.
     file_reader= csv.reader(election_data)
        # Read and print the header row.
     headers = next(file_reader)
     print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the election\n")
    txt_file.write("---------------------------\n")
    txt_file.write("Arapahoe\n Denver\n Jefferson")


