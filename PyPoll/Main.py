import pandas as pd
import os

#allow for inter-os compatability
votes_path = os.path.join("Resources", "election_data.csv")

#set data frame
voter_df = pd.read_csv(votes_path)

#find amount of votes cast
count = voter_df["Voter ID"].nunique()