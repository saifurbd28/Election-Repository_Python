# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0


# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}


# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_count = 0
winning_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # 3: Extract the county name from each row.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # the county list
        if county_name not in county_options:
            # 4b) Add the county name to the county list.
            county_options.append(county_name)
            # 4c) And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # 5) Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_options:
        total_votes = total_votes + 1
        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
         # 6d: Print the county results to the terminal.
        print = county_results
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)




        # For deliverable 2.
        #6f) write a decision statement that determines the county with the largest vote count and 
        # then adds that county and its vote count to the variables created in Step 2.
        # Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print ("winning_county_summary")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    
