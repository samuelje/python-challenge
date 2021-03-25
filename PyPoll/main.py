#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
    # 2-4 will be zipped lists using zip function

#Import modules
import os
import csv

# Open CSV and read CSV
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

