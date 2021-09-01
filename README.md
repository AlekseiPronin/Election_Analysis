# Election_Analysis

## Project Overview

A Colorado Board of Ellections employee has given us the task to complete the elections audit of a recent local Congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of voteseach candidate received.
4. calculate the percentage of votes each candidate won.
5. Determine the winner of the elction based on popular vote.

## Resources

- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code 1.59.1

## Data

The data in election_results.csv contained 3 columns: Ballot ID, County, Candidate.

## Summary

The result of the data analysis showed that:
- There were 369711 votes cast in the election.
- The election was held in three counties:
    - Jefferson
    - Denver
    - Arapahoe
- The results by counties were:
    - The votes in Jefferson county made 10.5% and 38855 votes of the total number of votes
    - The votes in Denver county made 82.8% and 306055 votes of the total number of votes
    - The votes in Arapahoe county made 6.7% and 24801 votes of the total number of votes
- The county with the largest turnover was Denver
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Candidate Charles Casper Stockham received 23.0% of the vote and 85,213 votes
    - Candidate Diana DeGette received 73.8% of the vote and 272,892 votes
    - Candidate Raymon Anthony Doane reveived 3.1% of the vote and 11,606 votes
- The winner of the election was :
    - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 votes

The output in the text file looks like this:

![](https://github.com/AlekseiPronin/Election_Analysis/blob/main/Resources/election_results.png)


## Election-Audit Summary

The code that was used for this analysis can be easily modified and used for any other elections. For example, if data contained gender information of voters, the code could be extended to see the breakdown of voters for each candidate or county. The same could be done if data set contained occupation information of voters. All this could be used to determine the target audience for candidates.

The script could also be used to make a deeper analysis of the current data set. For example, it could be modified to determine which candidate was more popular in which county.
