import csv
import os

#establish goal parameters
months_count = 0
revenue = 0
avg_rev_delta = 0
great_inc = 0
great_dec = 0

#use os path to join for compatability with other os'es (spelling?)
csvpath = os.path.join("Resources","budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvheader = next(csvreader)
    
    for row in csvreader:
        months_count += 1

        revenue += int(row[1])

print(months_count)
print(revenue)