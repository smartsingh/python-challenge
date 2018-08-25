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