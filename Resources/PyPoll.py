#The data we need to retrieve:
#1) total number of votes cast
#2) complete list of candidates who recieved votes
#3) the percentage of votes each candidate won
#4) the total number of votes each candidate won
#5) the winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     print(election_data)
     #Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     #Read and print the header row.
     headers = next(file_reader)
     print(headers)

# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")