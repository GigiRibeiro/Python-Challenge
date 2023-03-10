
import os
import csv

csv_file_path = ("PyPoll/election_data.csv")


total_votes = 0 
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0


with open(csv_file_path,newline="", encoding="utf-8") as elections:


    csvreader = csv.reader(elections,delimiter=",") 

    header = next(csvreader)     
    
    for row in csvreader: 
        
        total_votes +=1
            
        if row[2] == "Charles Casper Stockham": 
            Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Doane_votes +=1
         
candidates = ["Stockham", "DeGette", "Doane"]
votes = [Stockham_votes, DeGette_votes, Doane_votes]


dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


Stockham_percent = (Stockham_votes/total_votes) *100
DeGette_percent = (DeGette_votes/total_votes) * 100
Doane_percent = (Doane_votes/total_votes)* 100



print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Stockham:{Stockham_percent:.3f}% ({Stockham_votes})")
print(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Doane: {Doane_percent :.3f}% ({Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

output_file = "PyPoll/Election_Results_Analysis.txt"


with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
    file.write("\n")
    file.write(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
    file.write("\n")
    file.write(f"Doane: {Doane_percent :.3f}% ({Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
