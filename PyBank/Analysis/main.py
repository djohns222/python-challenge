#PyBank

import os

import csv

file_path = os.path.join("C:/Users/15132/OneDrive/Desktop/Resources/PyBank/budget_data.csv")

with open(file_path, mode="r") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter= ',')

#Skip firt row (headers)

    next(csv_reader)

#Calculate total amt of months/rev/dates

    months = 0
    Total_Rev = []
    dates = []

    for row in csv_reader:

        months += 1
        Total_Rev.append(int(row[1]))
        dates.append(row[0])


#Calculate Average 


Average_change = []

for m in range(1, len(Total_Rev)):
	change =  Total_Rev[m] - Total_Rev[m-1]
	Average_change.append(change)
Average = sum(Average_change)/len(Average_change)

#Greatest Increase in Profits

Greatest = max(Average_change)

#Greatest Decrease in Profits

Least = min(Average_change)

#Find corresponding month to increase/decrease

Greatest_inc_m = dates[Average_change.index(Greatest) + 1]
Greatest_dec_m = dates[Average_change.index(Least) + 1]

#Print Results to Text File

output_file = "PyBankresults.txt"


with open(output_file, 'w') as file:

    file.write("Financial Results\n")

    file.write("-------------------------------\n")

    file.write(f"Total Months: {months}\n")

    file.write(f"Total: $ {sum(Total_Rev)}\n")

    file.write(f"Average Change: ${Average:.2f}\n")

    file.write(f"Greatest Increase in Profits: {Greatest_inc_m} (${Greatest})\n") 

    file.write(f"Greatest Decrease in Profits: {Greatest_dec_m} (${Least})\n") 