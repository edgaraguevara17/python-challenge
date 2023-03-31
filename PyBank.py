import os
import csv

csvpath= os.path.join("../Resources/budget_data.csv")

#set starting points
months_count=0
prev_revenue=0
total_profloss= 0
month_change= []
revenue_changes=[]
months_list= []
revdelta_list= []
greatest_increase= ["", 0]
#sets output for greatest decrease, large number as starting point so any decrease is less than starting point hence new greatest decrease
greatest_decrease= ["", 9999999999999999999]


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    #loop through all the rows in the dataset
    for row in csvreader:
        #count the number of rows with data
        months_count=months_count+1
        #add the values in the second column
        total_profloss= total_profloss+ int(row[1])

        #revenue changes by month
        revenue_delta= int(row[1]) - prev_revenue
        prev_revenue= int(row[1])
        months_list= months_list + [row[0]]
        revdelta_list= revdelta_list + [row[1]]

        #is this row the new greatest increase? compare second value in list 'greatest_increase'
        if revenue_delta > int(greatest_increase[1]):
            #new first value in list is equal to value in first column of data set
            greatest_increase[0]= row[0]
            #new second value in list is equal to the delta of revenue from previous month
            greatest_increase[1]= row[1]

        if revenue_delta < int(greatest_decrease[1]):
            greatest_decrease[0]= row[0]
            greatest_decrease[1]= row[1]
#convert values in revdelta_list to integers (currently strings)
for i in range(len(revdelta_list)):
    revdelta_list[i]=int(revdelta_list[i])

average_delta= sum(revdelta_list)/ len(revdelta_list)

  
summary=\
    f"    Financial Analysis\n\
    -------------------------------\n\
    Total Months= {months_count}\n\
    Total= {total_profloss}\n\
    Average Change= {average_delta}\n\
    Greatest Increase in Profits = {greatest_increase}\n\
    Greatest Decrease in Profits = {greatest_decrease}"

print(summary)