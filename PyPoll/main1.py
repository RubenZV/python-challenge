import csv
import os
from csv import DictReader


tv = 0 
k = 0
cc = 0
l = 0
o = 0
with open('/Users/prophet60091/Desktop/PythonStuff/election_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    header = next(reader)
    for row in reader: 

        tv +=1

        if row['Candidate'] == "Khan": 
            k +=1
        elif row['Candidate'] == "Correy":
            cc +=1
        elif row['Candidate'] == "Li": 
            l +=1
        elif row['Candidate'] == "O'Tooley":
            o +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [k, cc,l,o]

dict= dict(zip(candidates,votes))
key = max(dict, key=dict.get)

kp = (k/tv) *100
cp = (cc/tv) * 100
lp = (l/tv)* 100
op = (o/tv) * 100

print(f"Election Results")
print(f"____________________________")
print(f"Total Votes: {tv}")
print(f"____________________________")
print(f"Khan: {kp:.3f}% ({k})")
print(f"Correy: {cp:.3f}% ({cc})")
print(f"Li: {lp:.3f}% ({l})")
print(f"O'Tooley: {op:.3f}% ({o})")
print(f"****************************")
print(f"Winner: {key}")
print(f"****************************")

output_file = "HW_RZV2.txt"

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"____________________________")
    file.write("\n")
    file.write(f"Total Votes: {tv}")
    file.write("\n")
    file.write(f"____________________________")
    file.write("\n")
    file.write(f"Khan: {kp:.3f}% ({k})")
    file.write("\n")
    file.write(f"Correy: {cp:.3f}% ({cc})")
    file.write("\n")
    file.write(f"Li: {lp:.3f}% ({l})")
    file.write("\n")
    file.write(f"O'Tooley: {op:.3f}% ({o})")
    file.write("\n")
    file.write(f"*****************************")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"*****************************")