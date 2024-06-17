#PyPoll

import os

import csv

file_path = os.path.join("C:/Users/15132/OneDrive/Desktop/Resources/PyPoll/election_data.csv")

with open(file_path, mode="r") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter= ',')

#Skip firt row (headers)

    next(csv_reader)

#Total number of votes cast

    Total = 0
    Candidate_votes = []
    Candidates = []

    for row in csv_reader:

        Total += 1
        Candidates.append(row[2])

#Find Candidate Names

    People = set(Candidates)
	
    C_1 = "Charles Casper Stockham"
    C_2 = "Diana DeGette"
    C_3 = "Raymon Anthony Doane"


#Count Total number of votes for each candidate 

    C1_count = Candidates.count(C_1)
    C2_count = Candidates.count(C_2)
    C3_count = Candidates.count(C_3)


#Calculate percentage of each candidiate

    C1_p = (C1_count/Total) *100
    C2_p = (C2_count/Total) *100
    C3_p = (C3_count/Total) *100
   


#Determine Winner


if C1_count > C2_count and C1_count > C3_count:
	winner = "Charles Casper Stockham"
elif C2_count > C1_count and C2_count > C3_count:
	winner = "Diana DeGette"
elif C3_count > C1_count and C3_count > C2_count:
	winner = "Raymon Anthony Doane"
else:
	winner = "Tie"



#Print Results to Text File

with open('PyPollresults.txt', 'w') as file:

    file.write("Election Results\n")

    file.write("-------------------------------\n")

    file.write(f"Total Votes: {Total}\n") 

    file.write("-------------------------------\n")

    file.write(f"{C_1}: {C1_p:.3f}% ({C1_count})\n")

    file.write(f"{C_2}: {C2_p:.3f}% ({C2_count})\n")

    file.write(f"{C_3}: {C3_p:.3f}% ({C3_count})\n") 

    file.write("-------------------------------\n")

    file.write(f"Winner: {winner}\n") 

    file.write("-------------------------------\n")
