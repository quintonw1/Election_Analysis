import os 
import csv
# Generating File variables 
file_to_open = os.path.join("Election_Analysis", "Resources", "election_results.csv")
file_to_save = os.path.join("Election_Analysis", "Analysis", "Election_analysis.txt")

# Initializing Variables used for analysis 
total_votes = 0 

#county data variables 
County_options = []
County_name = ""
county_votes = {}
winning_county = "" 
winning_count_county = 0 

#candidate data variables
Candidate_options = []
candidate_name = ""
candidate_votes = {}
winning_candidate = "" 
winning_count = 0 
winning_percentage = 0

# Printing header 
print(f"------------------------------\n"
f"Election Results\n"
f"------------------------------\n")

# opening data file and populating dictionaries for counties and candidates 
with open(file_to_open) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:

        county_name = row[1]
        candidate_name = row[2]

        total_votes = total_votes + 1

        if county_name not in County_options:
            County_options.append(county_name)
            county_votes[county_name] = 0 
        
        county_votes[county_name] += 1 

        if candidate_name not in Candidate_options:
            Candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 
        
        candidate_votes[candidate_name]+= 1 

# Analyizing data to determine winning county and candidate while exporting data into a txt file 
with open(file_to_save, "w") as txt_file: 
    # creating election results string 
    Election_results = (f"\nElection Results\n"
    f"------------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"------------------------------\n"
    f"\nCounty Votes:\n")

    # writing election results into txt file 
    txt_file.write(Election_results)

    # determining which county had most votes and then printing and writing into txt file 
    for county in county_votes: 
        votes = county_votes[county]
        vote_percentage = int(votes) / int(total_votes) *100 
        if votes>winning_count_county: 
            winning_count_county = votes
            winning_county = county 
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(f"{county}: {vote_percentage:.1f}% ({votes:,})")
        txt_file.write(county_results)

    winning_county_summary = (f"\n------------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"------------------------------\n")

    txt_file.write(winning_county_summary)
    print(winning_county_summary)
    
    # determining which candidate had most votes and then printing and writing data into txt file 
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
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

#closing txt file 
txt_file.close()






