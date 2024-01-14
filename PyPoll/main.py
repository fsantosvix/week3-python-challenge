#import modules
import os
import csv


# define the path of the csv file to be used
file = 'Resources/election_data.csv'

#define the containers to store data from the csv file
ballot_list = []
county_list = []
candidate_list = []

# open and read the csv file
with open (file) as csvfile:
    pyPollFile = csv.reader(csvfile)
    # print (pyPollFile)
    
    # read the header row
    csv_header = next(pyPollFile)
    # print (csv_header)
    
    # add records from the csv file into the container as lists
    for row in pyPollFile:
        ballot_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])
        
    #count the total number of votes
    total_votes = len(ballot_list)
    # print(total_votes)
    

    #find the complete list of candidates - convert the list into a set
    unique_candidates = set(candidate_list)
    #print(unique_candidates)
    #print(len(unique_candidates))

#find the total number of votes each candidate won

votes_Diana = 0
votes_Raymon = 0
votes_Charles = 0

for items in candidate_list:
    if items == 'Diana DeGette':
        votes_Diana += 1
    if items == 'Raymon Anthony Doane':
        votes_Raymon += 1
    if items == 'Charles Casper Stockham':
        votes_Charles += 1

# print(votes_Diana)
# print(votes_Raymon)
# print(votes_Charles)

#percentage of votes each candidate won
percentage_Diana = round((votes_Diana / total_votes * 100),3)
percentage_Raymon = round((votes_Raymon / total_votes * 100),3)
percentage_Charles = round((votes_Charles / total_votes * 100),3)

# print(percentage_Diana)
# print(percentage_Raymon)
# print(percentage_Charles)

#define winner comparing the votes variables
if (votes_Charles > votes_Diana) and (votes_Charles > votes_Raymon):
    winner = 'Charles Casper Stockham'
elif (votes_Raymon > votes_Diana) and (votes_Raymon > votes_Charles):
    winner = 'Raymon Anthony Doane'
elif (votes_Diana > votes_Charles) and (votes_Diana > votes_Raymon):
    winner = 'Diana DeGette'
# print (winner)

#print final analysis to the console/terminal
a = 'Election Results\n'
b = '-------------------------\n'
c = f'Total Votes: {total_votes}\n'
d = f'Charles Casper Stockham: {percentage_Charles}% ({votes_Charles})\n'
e = f'Raymon Anthony Doane: {percentage_Raymon}% ({votes_Raymon})\n'
f = f'Diana DeGette: {percentage_Diana}% ({votes_Diana})\n'
g = f'Winner: {winner}\n'

print(a)
print(b)
print(c)
print(b)
print(d)
print(e)
print(f)
print(b)
print(g)
print(b)


#export the Analysis to a text file

#set the text as a list to be exported to the txt file
analysis_list = [a,b,c,b,d,e,f,b,g,b]

#set the path to the exported file
output_results = os.path.join('Analysis/results.txt')

#write the lines from the list into the txt file and close it
with open(output_results, 'w') as txtfile:
    output = txtfile.writelines(analysis_list)
    txtfile.close()