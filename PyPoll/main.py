#Import necessary:
import os
import csv

#Set file location:
csvpath= os.path.join("election_data.csv")

#Open file:
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

        #Name variable:
        candidate=row[2]

        #Put first vote for candidate in dictionary:
        if candidate not in candidate_votes:
            candidate_votes[candidate]=1

        #Add additional votes to dictionary:
        else:
            candidate_votes[candidate]=candidate_votes[candidate]+1

    #Set initial variable to zero:
    winning_votes=0

    #Print title and total votes:
    print("")
    print("Election Results")
    print("")
    print("----------------------------------------")
    print("")
    print(f"Total Votes: {total_votes}")
    print("")
    print("----------------------------------------")

    #Print title and total votes to text file:
    text_file = open("PyPoll_Output.txt", "w")
    text_file.writelines(["Election Results \n", "---------------- \n", f"Total Votes: {total_votes} \n",
        "---------------- \n"])
    text_file.close()

    #Iterate through candidate dictionary to calculate and print percent votes:
    #Also append text file:
    edit_text=open("PyPoll_Output.txt", "a")
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percent_votes=(votes/total_votes)*100
        percent_votes=round(percent_votes, 2)
        print("")
        print(f"{candidate}: {percent_votes}% ({candidate_votes[candidate]})")
        print("")
        edit_text.writelines([f"{candidate}: {percent_votes}% ({candidate_votes[candidate]}) \n"])

        #Also find winner:
        if votes>winning_votes:
            winning_votes=votes
            winner=candidate

    #Print final result:
    print("----------------------------------------")
    print("")
    print (f"The winner is {winner}!")
    print("")
    print("----------------------------------------")
    print("")

    #Add final result to text file and close:
    edit_text.writelines(["---------------- \n", f"The winner is {winner}! \n", "---------------- \n" ])
    edit_text.close()

