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

        #find greatest increases/decreases and their months
        if int(row[1]) > great_inc:
            great_inc = int(row[1])
            great_inc_month = row[0]
        elif int(row[1]) < great_dec:
            great_dec = int(row[1])
            great_dec_month = row[0]
        


    for row in range(1,len(changes)):
        change_sum += changes[row]
        
    avg_rev_delta = round((change_sum / (months_count - 1)),2)


print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months_count))
print("Total: $" + str(revenue))
print("Average Change: $" + str(avg_rev_delta))
print("Greatest Increase in Profits: " + great_inc_month + " ($" + str(great_inc) +")")
print("Greatest Decrease in Profits: " + great_dec_month + " ($" + str(great_dec) +")")
