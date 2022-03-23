# Election-Repository_Python
Overview of Election audit:
The election commission has requested some additional data to complete the election audit of a recent election. These are:
•	The voter turnout for each county
•	The percentage of votes from each county out of the total count
•	The county with the highest turnout
Election-Audit Results:
The Election-Audit was done using python code. The election analysis txt file contains the details of the result. 
o	How many votes were cast in this congressional election?
-	Total Votes: 369,711

o	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
-	Jefferson: 10.5% (38,855)
-	Denver: 82.8% (306,055)
-	Arapahoe: 6.7% (24,801)

o	Which county had the largest number of votes?
-	Denver

o	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
-	Charles Casper Stockham: 23.0% (85,213)
-	Diana DeGette: 73.8% (272,892)
-	Raymon Anthony Doane: 3.1% (11,606)

o	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
-	Winner: Diana DeGette
-	Winning Vote Count: 272,892
-	Winning Percentage: 73.8%

Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This python script is versatile and easy to adopt in any elections. For example,
1)	To know the vote count of the 2nd position, we can modify the code following ways:
2)	# Track the 2nd winner candidate, vote count, and percentage.
3)	2nd_candidate = ""
4)	2ndWinner_count = 0
5)	2ndWinner_percentage = 0

	 # And begin tracking that 2nd candidate's voter count.
            candidate_votes[2nd_candidate] = 0
        # Add a vote to that candidate's count.
        candidate_votes[2nd_candidate] += 1

2)To know the vote percentate of the 2nd position, we can modify the code following ways:
	 # 6b: Retrieve the 2nd candidtate vote count.
        votes = candidate_votes[2nd_candidate]
        # 6c: Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

