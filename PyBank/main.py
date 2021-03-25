#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#Modules
import os
import csv

#CSV path and open/read CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

#with open(csvpath) as csvfile:
    
#    csvreader = csv.reader(csvfile, delimiter=',')

#   print(csvreader)

#    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

#    for row in csvreader:
 #       print(row)

#lists to store data
date = []
#month = []
#year = []
#Profits = []
#Losses = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
#       Split date to get month only separated from year
        date.append(row[0])
        month_only = row[0].split("-")
#        print(month_only)
        total_months = len(list(month_only))
        print(total_months)
       

#Final outputs