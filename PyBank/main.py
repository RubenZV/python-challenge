import csv
import os
from csv import DictReader


mo=[]
pl = []
change=[]
with open('/Users/prophet60091/Desktop/PythonStuff/HW1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    header = next(reader) 
    for row in reader:
        mo.append(row['Date'])
        pl.append(float(row['Profit/Losses']))
    for r in range(len(pl)-1):
        change.append(pl[r+1]-pl[r])

inc_value = max(change)
dec_value = min(change)

inc_month = change.index(max(change)) + 1
dec_month = change.index(min(change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(mo)}")
print(f"Total: ${sum(pl)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {mo[inc_month]} (${(str(inc_value))})")
print(f"Greatest Decrease in Profits: {mo[dec_month]} (${(str(dec_value))})")

output_file = ("HW_rzvBank.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(mo)}")
    file.write("\n")
    file.write(f"Total: ${sum(pl)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change)/len(change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {mo[inc_month]} (${(str(inc_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {mo[dec_month]} (${(str(dec_value))})")