import os 
import csv

file_to_open = os.path.join("Election_Analysis", "Resources", "election_results.csv")
file_to_save = os.path.join("Election_Analysis", "Analysis", "Election_analysis.txt")


total_votes = 0 

Candidate_options = []
candidate_name = ""

candidate_votes = {}

winning_candidate = "" 
winning_count = 0 
winning_percentage = 0
print(f"------------------------------\n"
f"Election Results\n"
f"------------------------------\n")
with open(file_to_open) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        candidate_name = row[2]
        
        total_votes = total_votes + 1

        if candidate_name not in Candidate_options:
            Candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        
        candidate_votes[candidate_name]+= 1 

with open(file_to_save, "w") as txt_file: 

    Election_results = (f"\nElection Results\n"
    f"------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------------\n"
    f"")
    txt_file.write(Election_results)

    for candidate in candidate_votes: 
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) *100 
        if votes>winning_count and vote_percentage>winning_percentage: 
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate 
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})")
        txt_file.write(candidate_results)

    winning_candidate_summary = (f"------------------------------\n"
    f"Winning Candiate: {winning_candidate}\n"
    f"Winning Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")
    txt_file.write(winning_candidate_summary)

    



txt_file.close()


print(winning_candidate_summary)



#print(candidate_votes)
#print(Candidate_options)
#print(total_votes)

    

   



# election_data.close()


