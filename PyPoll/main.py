#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
    # 2-4 will be zipped lists using zip function

#Import modules
import os
import csv

# Create variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# Open CSV and read CSV
csvpath = os.path.join('Resources', 'election_data.csv')

#Open and read csv file
with open(csvpath) as csvfile:

#   Create csvreader variable to store contents of election_data.csv file    
    csvreader = csv.reader(csvfile, delimiter=',')

#   Skip header labels in order to interpret values
    header = next(csvreader)

#   Iterate through the rows in the csvreader variable stored contents
    for row in csvreader:

#       Count the unique voter IDs and store in variable called total_votes
        total_votes +=1

#       if statements to compile all votes mathching a candidate and adding them to cadidate's variable
        if row[2] == "Khan":
            Khan_votes +=1
        elif row[2] == "Correy":
            Correy_votes +=1
        elif row[2] == "Li":
            Li_votes +=1
        elif row[2] == "O'Tooley":
            OTooley_votes +=1

# To find the winner, create dictionaries of the two lists previously created
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [Khan_votes, Correy_votes, Li_votes, OTooley_votes]

# Zip together the lists of candidates and the total votes
# Use max function of dictionary to return the winner
dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)

# Percentage of votes by candidate
Khan_percent = (Khan_votes/total_votes) *100
Correy_percent = (Correy_votes/total_votes) *100
Li_percent =(Li_votes/total_votes) *100
OTooley_percent = (OTooley_votes/total_votes) *100

#Final Statements
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
print(f"Li: {Li_percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_votes})")
print(f"-------------------------")
print(f"Winner: {key}")
print(f"-------------------------")

# Output file path
output_file = os.path.join("analysis", "PyPoll_Analysis_Summary")

with open(output_file, "w") as file:

#   Print final statements to PyPoll_Analysis_Summary 
    file.write("Election Results")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Khan: {Khan_percent:.3f}% ({Khan_votes})")
    file.write("\n")
    file.write(f"Correy: {Correy_percent:.3f}% ({Correy_votes})")
    file.write("\n")
    file.write(f"Li: {Li_percent:.3f}% ({Li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_votes})")
    file.write("\n")
    file.write(f"-------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"-------------------------")