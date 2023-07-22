import os
import csv

#Create Variables / Arrays
Total_months = 0
last_month = 0
net_total = 0
current_month = []
months = []



csvpath = os.path.join('..', '(3)_PyBank_PyPoll', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
#The total number of months included in the dataset
    for data in csvreader:
        Total_months = Total_months + 1
        
#net total amount of "Profit/Losses" over the entire period
        net_total = net_total + int(data[1])
        
#The changes in "Profit/Losses" over the entire period
        total_change = int(data[1]) - last_month
        current_month.append(total_change)
        last_month = int(data[1])
        
# The average changes of those months
        average_change = (net_total/Total_months)
        
#The greatest increase in profits (date and amount) over the entire period
        months.append(data[0])
        great_in = max(current_month)
        great_in_m = months[current_month.index(great_in)]
        
#The greatest decrease in profits (date and amount) over the entire period
        great_de = min(current_month)
        great_de_m = months[current_month.index(great_de)]

#Analysis
print(f"Financial Analysis")
print("------------------------")
print(f"Total Months: {Total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {great_in_m}")
print(f"Greatest Decrease in Profits: {great_de_m}")
