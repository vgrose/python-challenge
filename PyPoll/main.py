#Import necessary:
import os
import csv
#Set file location:
csvpath= os.path.join("election_data.csv")
with open(csvpath) as csvfile:
    #Separate each column at comma:
    election_data = csv.reader(csvfile, delimiter=',')
    #Skip header:
    csv_header = next(election_data)
    #Set initial votes to zero and create an empty dictionary for candidates:
    total_votes=0
    candidate_votes={}
    #Iterate over rows:
    for row in election_data:
        #Add up total votes:
        total_votes=total_votes+1
        candidate=row[2]
        if candidate not in candidate_votes:
            
            candidate_votes[candidate]=1
        else:
            candidate_votes[candidate]=candidate_votes[candidate]+1
    winning_votes=0



    print("")
    print("Election Results")
    print("")
    print("----------------------------------------")
    print("")
    print(f"Total Votes: {total_votes}")
    print("")
    print("----------------------------------------")
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percent_votes=(votes/total_votes)*100
        percent_votes=round(percent_votes, 2)
        print("")
        print(f"{candidate}: {percent_votes}% ({candidate_votes[candidate]})")
        print("")
        if votes>winning_votes:
            winning_votes=votes
            winner=candidate
    
    print("--------------------------------------")
    print("")
    print (f"Winner: {winner}")
    print("")
    print("-------------------------------------")

    
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
