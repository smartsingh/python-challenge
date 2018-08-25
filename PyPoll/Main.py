import pandas as pd
import os

#allow for inter-os compatability
votes_path = os.path.join("Resources", "election_data.csv")

#set data frame
voter_df = pd.read_csv(votes_path)

#find amount of votes cast
count = voter_df["Voter ID"].nunique()

#grab totals for all candidates
candi_totals = voter_df["Candidate"].value_counts()

#arrange totals to see results in order (e.g., 1st place, 2nd, etc.)
results = pd.DataFrame(candi_totals.sort_values(ascending = False))

#grab names of all candidates, in order of place
candi_list = results.index.tolist()

#set winner to first name in list
winner = candi_list[0]

#grab votes to a list
candi_votes = results["Candidate"].tolist()

#create percentages for each candidate
candi_perc = [(int(x)/int(count))*100 for x in candi_votes ]

#format percentages
candi_perc = [format(x, '.2f') for x in candi_perc]

#results
print("-------------------------")
print("Election Results")
print("-------------------------")
print("Total Votes :" + str(count))
print("-------------------------")

#since we know that all the positions across all the lists come from the same data frame and the same order,
#we can iterate over all three lists using the same integer for the place of each item and get the correct values
for i in range(0,4):
    print(candi_list[i]+ ": " + str(candi_perc[i]) + "% (" + str(candi_votes[i]) + ")")
    
#print winner
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#write results to txt file
writepath = os.path.join("Resources", "results.txt")

with open(writepath, "w") as textfile:
    textfile.write("-------------------------")
    textfile.write("\nElection Results")
    textfile.write("\n-------------------------")
    textfile.write("\nTotal Votes :" + str(count))
    textfile.write("\n-------------------------\n")
    
    for i in range(0,4):
        textfile.write(candi_list[i]+ ": " + str(candi_perc[i]) + "% (" + str(candi_votes[i]) + ")\n")
    textfile.write("-------------------------\n")
    textfile.write("Winner: " + winner)
    textfile.write("\n-------------------------")

print(".")
print(".")
print(".")
print("A text file has been created and stored in " + writepath + " for your convenience. Congratulaions " + winner + "!")