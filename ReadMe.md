# Election Analysis
### Project Overview
A colorado board of election employees has given me he task to complete the elecion audit of a recent local congressional election.
  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate and individual counties received.
  4. Calculate the percentage of votes each candidate and individual counties won.
  5. Determine the winner of the election based on popular vote and the county with the highest votes.


### Resources
####  - Data Source: election_results.csv
####  - Software: Python 3.10.1, Visual Studio Code
  
## Challenge Overview
#### The analysis of the election show that:
#### There were 369,711 total votes.
#### The Candidates Were:
    -Charles Casper Stockham
    -Diana DeGette
    -Raymon Anthony Doane
#### The candidate results were:
    -Charles Casper Stockham received 23% of the vote for 85,213 votes.
    -Diana DeGette received 73.8% of the vote for 272,892 votes.
    -Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
#### The winner of the election was:
    -Diana DeGette, who received 73.8% of the vote for 272,892 votes.
#### The largest county turnout was Denver.
    -Jefferson received 10.5% of the vote for 38,855 votes.
    -Denver received 82.8% of the vote for 306,055 votes.
    -Arapahoe received 6.7% of the vote for 24,801 votes.

The purpose of this challenge was to figure out how to calculate, print and save output data to the terminal and text file. Throughout this challenge many difficulties arrised including how to connect a csv file to the code and how to get the percise output you wanted. If the .py file was not in the right folder or directory it would not be able to run because of the lack of data to process. The task that was asked of us was to calculate the total number of votes cast, get a complete list of candidates and counties which received votes and or where the votes were cast. Calculate the total number of votes each candidate received. Calculate the total number of votes cast in each county. Calculate these vote values into percentages. Determine which candidate won the election with how many votes and what percentage of vote, and lastly determine which county had the most votes cast.

## Challenge Summary
This election analysis code can work for almost any dataset, aslong as the data set has the county listed in column 2 of the excel sheet and the person voted for is listed in colum 3. The only real things you'd have to make sure of is to have the code modified to the proper directory and the proper file used from that directory. For example this file has 2 folders connected to it one being the "Resource" folder which hold the spreadsheet where the data comes from. You would have to have a resource folder with your data file in it and the file name listed like this one with "election_results.csv" (no spaces in file name). As for the output it will be put into a txt document in the "Analysis: folder which should also be in the same directory. You can change the text file name to whatever you would like it to be called and it will auto generate a new file if no file is there. Please refer below for where to change the file to change the data set used.
![image1](https://github.com/Ajsforlife/Election_Analysis/blob/main/module%203/pypoll%20file%20connection%20.png)
You can also modify the output you receiveby changing the orange words in the quotation marks but dont touch anything after the \n.
You can make these outputs say whatever you like just dont change the things that aren't in orange or the code itself won't work properly.
![image2](https://github.com/Ajsforlife/Election_Analysis/blob/main/module%203/Screenshot%202022-06-15%20152212.png)
![image3](https://github.com/Ajsforlife/Election_Analysis/blob/main/module%203/Screenshot%202022-06-15%20152230.png)

Overall the code should work with any dataset assuming the above is properly input.

