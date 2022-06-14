# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
#add our dependencies
import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#create a filenme variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initialize the total vote counter.
total_votes = 0
#candidate options
candidate_options = []
#candidate votes, empty dictionary
candidate_votes = {}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and the the file.
with open(file_to_load) as election_data:

    #read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)

    #print each row in the csv file.
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        #if candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates/
            candidate_options.append(candidate_name)
            #begin tracking he candidate's vote count.
            candidate_votes[candidate_name] = 0
        #add a vote to each candidate's count
        candidate_votes[candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
         # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        #determine if the votes are greater then the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning_count = votes and winning_percet = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name
    #print out the winning candidate vote count and percentage to terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)
