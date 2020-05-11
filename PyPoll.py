import os 
import csv

file_to_open = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "Election_analysis.txt")

with open(file_to_open) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    print(headers)



# election_data.close()

#with open(file_to_save, "w") as txt_file: 
    #txt_file.write("ARapahoe\nDenver\nJefferson")

#txt_file.close()

