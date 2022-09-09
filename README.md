# Election_Analysis
## Project Overview
A Colorado Board of Elections empolyee has given you the following tasks to complete the election audit of recent local congressional election.
1. Calculate The total number of votes cast
2. Get A complete list of candidates who received votes
3. Calculate The percentage of votes each candidate won
4. Calculate The total number of votes each candidate won
5. Calculate The winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv
* Software: Python 3.9.1, Visual Studio Code 1.52.1

## Summary
The analysis of the election shows that:

* There were 369,711 votes cast in the election.

* The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
    
* The candidate results were:
    * Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
    * Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
    * Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.
    
* The winner of the election was:
     * Diana DeGette, who received 73.8% of the vote for a total of 272,892 votes.
     
* The voter turnout for each county was:
    * Jefferson produced 10.5% of voters, for a total of 38,855 voters.
    * Denver produced 82.8% of voters, for a total of 306,055 voters.
    * Arapahoe produced 6.7% of voters, for a total of 24,801 voters.
    
* The county with the largest voter turnout was:
    * Denver, which produced 82.8% of voters, for a total of 306,055 voters.
    
 ## Challenge Summary
 I propose that the election commission can use the PyPoll.py script, with some modifications, for other elections. Currently, the program is written to analyze the election_results.csv file by iterating through each row and reading the data in the second and third columns, 'County' and 'Candidate', in order to calculate and print the results. There are many different ways in which this code can be altered and used with any election results.
