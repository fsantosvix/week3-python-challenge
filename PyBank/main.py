#import modules
import os
import csv

# define the path of the csv file to be used
file_path = 'Resources/budget_data.csv'

months_list = []
profit_loss_list = []
profit_loss_changes = []

# open and read the csv file
with open (file_path) as csv_file:
    pyBank = csv.reader(csv_file)
    # print (pyBank)

    # read the header row
    csv_header = next(pyBank)
    # print (csv_header)
    
    # add records from the csv file into lists
    for row in pyBank:
        months_list.append(row[0])
        profit_loss_list.append(int(row[1]))
    
    #count and print the number of months
    total_months = len(months_list)
    # print(total_months)   

    #find the net amount of Profit/Lost over the period
    total_profit_loss = sum(profit_loss_list)
    # print(total_profit_loss)

#identify the changes in Profit/Losses for each month
i = 1
while i <= (len(profit_loss_list)-1):
    change = profit_loss_list[i] - profit_loss_list[i-1]
    profit_loss_changes.append(change)
    # print(change)
    i = i+1
    

#find the average of the profit/losses over the period
#the total number of observations is the total number of months minus 1
average_profit_loss = round((sum(profit_loss_changes)/(total_months-1)),2)
# average_profit_loss

#identify the greatest increase value within the profit/losses list
greatest_increase = max(profit_loss_changes)
# greatest_increase

#identify the index of the greatest value in the profit/loss list
index_greatest_inc = profit_loss_changes.index(greatest_increase)
# index_greatest_inc

#identify the respective item in the months list (it is the index + 1 as the profit/loss list has one item less
greatest_inc_month = months_list[index_greatest_inc + 1]
# greatest_inc_month

#identify the greatest decrease value within the profit/losses list
greatest_decrease = min(profit_loss_changes)
# greatest_decrease

#identify the index of the greatest value in the profit/loss list
index_greatest_dec = profit_loss_changes.index(greatest_decrease)
# index_greatest_dec

#identify the respective item in the months list (it is the index + 1 as the profit/loss list has one item less
greatest_dec_month = months_list[index_greatest_dec + 1]
# greatest_dec_month

#print final analysis to the console/terminal
a = 'Financial Analysis\n'
b = '===================================\n'
c = f'Total Months: {total_months}\n'
d = f'Total: ${total_profit_loss}\n'
e = f'Average Change: ${average_profit_loss}\n'
f = f'Greatest Increase in Profits: {greatest_inc_month} (${greatest_increase})\n'
g = f'Greatest Decrease in Profits: {greatest_dec_month} (${greatest_decrease})\n'


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


#export the Analysis to a text file

#set the text as a list to be exported to the txt file
analysis_list = [a,b,c,d,e,f,g]

#set the path to the exported file
out_analysis = os.path.join('Analysis/output_analysis.txt')

with open (out_analysis, 'w') as txtFile:
    #write the lines from the list into the txt file and close it
    txtwriter = txtFile.writelines(analysis_list)
    txtFile.close()
    