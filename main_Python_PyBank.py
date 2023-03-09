import os
import csv

csv_file_path = ("Instructions/PyBank/budget_data.csv")

total_months=[]
total_profit= []
montly_profit_change=[]

with open(csv_file_path,newline="",encoding="utf-8") as budget:

    csvreader = csv.reader(budget,delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        montly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(montly_profit_change)
max_decrease_value = min(montly_profit_change)

max_increase_month = montly_profit_change.index(max(montly_profit_change))+1
max_decrease_month = montly_profit_change.index(min(montly_profit_change))+1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum( montly_profit_change)/len(montly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = ("Instructions/PyBank/Financial_Analysis_Summary.txt")

with open(output_file,'w') as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(montly_profit_change)/len(montly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
 