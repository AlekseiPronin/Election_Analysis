# the data we need to retrieve

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the ellection based on popular vote

# Direct path
# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     # To do: perform analysis
#      print(election_data)


# #Indirect path
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     # To do: perform analysis
#      print(election_data)




# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

#Declaring candidate options
candidate_options = []

#Declaring the empty dictionary of candidates' votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]

        # if the candidate doesn't match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to candidate options
            candidate_options.append(candidate_name)

            #begin tracking each candidate's votes
            candidate_votes[candidate_name] = 0

        #add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # # Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")


    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name 


#  To do: print out the winning candidate, vote count and percentage to terminal.

    for candidate in candidate_votes:
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)