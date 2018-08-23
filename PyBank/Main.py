import csv
import os

#establish goal parameters (i.e., total months, sum of revenue, etc)
months_count = 0
revenue = 0

#for use with changes in between months
current = 0
previous = 0
changes = []
change_sum = 0
avg_rev_delta = 0

#for use with finding increase/decrease
great_inc = 0
great_inc_month = ""
great_dec = 0
great_dec_month = ""

#use os path to join for compatability with other os'es (spelling?)
csvpath = os.path.join("Resources","budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvheader = next(csvreader)
    
    for row in csvreader:
        #count months
        months_count += 1

        #sum revenue
        revenue += int(row[1])

        #create list of changes to be used later
        current = int(row[1])

        changes.append(current - previous)

        previous = int(row[1])

    for row in range(1,len(changes)):
        change_sum += changes[row]
        
    avg_rev_delta = round((change_sum / (months_count - 1)),2)

print(months_count)
print(revenue)
print(avg_rev_delta)