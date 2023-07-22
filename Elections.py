import os
import csv

#Create Variables / Arrays
total_votes = 0
vote_count_for_1 = 0
vote_count_for_2 = 0
vote_count_for_3 = 0
candidates = []
vote_percent = []
vote_per_p = {}



csvpath = os.path.join('..', '(3)_PyBank_PyPoll', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    election_data = list(csvreader)

#The total number of votes cast
    for data in election_data:
        total_votes = total_votes + 1
        politician = data[2]
        
        
#A complete list of candidates who received votes
        if politician not in candidates:
           candidates.append(politician)
           vote_per_p[politician] = 0
           vote_per_p[politician] = vote_per_p[politician] + 1
        
        
#The total number of votes each candidate won
    for data in election_data:
        politician1 = candidates[0]
        politician2 = candidates[1]
        politician3 = candidates[2]
        if data[2] == politician1:
            vote_count_for_1 += 1
        if data[2] == politician2:
            vote_count_for_2 += 1
        if data[2] == politician3:
            vote_count_for_3 += 1
   
#The percentage of votes each candidate won
vote_percent_pol_1 = (vote_count_for_1/total_votes) *100
vote_percent_pol_2 = (vote_count_for_2/total_votes) *100
vote_percent_pol_3 = (vote_count_for_3/total_votes) *100


#The winner of the election based on popular vote

Max= max(vote_count_for_1,vote_count_for_2,vote_count_for_3)

if Max == vote_count_for_1:
    winner = candidates[0]
elif Max == vote_count_for_2:
    winner = candidates[1]
elif Max == vote_count_for_3:
    winner = candidates[2]


print(f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates[0]}: {vote_percent_pol_1} ({vote_count_for_1})
{candidates[1]}: {vote_percent_pol_1} ({vote_count_for_2})
{candidates[2]}: {vote_percent_pol_1} ({vote_count_for_3})
-------------------------
Winner: {winner}
-------------------------""")








