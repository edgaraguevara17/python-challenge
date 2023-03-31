#import csv reading dependencies
import os
import csv 

csvpath= os.path.join("/Users/edgarguevara/Desktop/data/homework/python-challenge/Python_Homework/PyPoll/Resources/election_data.csv")

#define variables and starting points for vote counts, create a list of candidates in dataset
votecount = 0 
candidate_list= []
candidate_votes= {}
winner= ""
winner_votecount= 0


with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    headers= next(csvfile)

#loop through every row in the dataset
    for row in csvreader:
        votecount= votecount+1
        candidate= row[2]
        if candidate not in candidate_list:
            #adds new name to candidate list
            candidate_list.append(candidate)
            #sets new candidate's initial vote count to zero
            candidate_votes[candidate]= 0
            #adds 1 to that candidates vote count
        candidate_votes[candidate] = candidate_votes[candidate]+1



#print to terminal
summary= \
 f"Election Results\n\
-----------------------------\n\
Total Votes= {votecount}\n\
----------------------------"
print(summary)       


#find calculate vote count and percentage per candidate
voter_output = ""
for name in candidate_votes:
    votes= candidate_votes.get(name)
    vote_percent= (float(votes)/ float(votecount))* 100

    if votes> winner_votecount:
        winner_votecount=votes
        winner= name

    voter_output= f"{name}: {vote_percent: .3f}% ({votes})\n"
    print(voter_output)

#print to terminal
winner_summary=(
    f"------------------\n"
    f"Winner: {winner}\n"
    f"--------------------"
)
print(winner_summary)

#print final output to a txt file
output_file= "output_PyPoll.txt"

with open(output_file, 'w') as file:
    file.write(summary)
    file.write(voter_output)
    file.write(winner_summary)
    print(f"the summary has been saved to {output_file}")


