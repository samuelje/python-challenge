#Import modules
import os
import csv

#csv path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create empty lists to iterate through specific rows for a given variable
total_months = []
total_profit = []
monthly_profit_change = []

#Open/read csv file
with open(csvpath, newline='') as csvfile:

#   Create csvreader variable to store contents of budget.csv file
    csvreader = csv.reader(csvfile, delimiter=",")

#   Skip header labels in order to interpret values
    header = next(csvreader)

#   Iterate through the rows in the csvreader variables stored contents
    for row in csvreader:

#       Split date to get month only separated from year
        total_months.append(row[0])
        total_profit.append(int(row[1]))

#   Loop through the profits to get monthly change in profits
    for i in range(len(total_profit)-1):

#       Find difference between given two months and append to monthly profit change list
        monthly_profit_change.append(total_profit[i+1] - total_profit[i])

#Calculate max and min from monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

#Correlate max and min values to proper month list and index
#Use + 1 to associate change with "next" month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#Final statements

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
