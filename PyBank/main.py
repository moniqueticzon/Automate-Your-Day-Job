# Imports needed to execute script
from pathlib import Path
import csv

# Set the file path
csvpath = Path("Data/budget_data.csv")

# Open the file and use reader to return each row of the csv file 
file = open(csvpath)
csv_reader = csv.reader(file)

# Read the header row
header = next(csv_reader)

# Initiate lists to be used
data = []
changes = []
dates = []

# Initiate variables to be used
avg_change = 0
total_change = 0
total_profit = 0
month_count = 0

for row in csv_reader:

    date = row[0]
    profit = int(row[1])
    
    # Append the date and profit to the data list
    data.append([date, profit])
    
    # Calculate the total profit and assign it to total_profit
    total_profit += profit
    
    # Return the total number of months in the data and assign it to month_count
    month_count = len(data)

# Set an output path for a new csv that contains data for the remaining calculations
output_path = Path("Outputs/output_main.csv")

# Open the file to write the remaining calculations results
file = open(output_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Change"])

for i in range(len(data)-1):
    current_month_row = data[i+1]
    current_month_date = current_month_row[0]
    current_month_profit = current_month_row[-1]
    last_month_row = data[i]
    last_month_profit = last_month_row[-1]
    
    # Calculate the monthly_change in profits/losses
    monthly_change = (current_month_profit - last_month_profit)
    
    # Calculate the total_change in profits/losses by summing the monthly_change in profits/losses
    total_change += monthly_change
    
    # Write the current_month_date and the monthly_change data to the output_main.csv
    writer.writerow([current_month_date, monthly_change])

    # Append the calculated monthly_change to the changes list
    changes.append([monthly_change])
    
    # Append the dates corresponding with the monthly_change amounts to the dates list
    dates.append([current_month_date])

    # Calculate the average change in profits/losses over the whole period
    avg_change = round(total_change / len(changes), 2)
    
# Use the minimum and maximum to return the greatest increase and greatest decrease in profits from the changes list
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Return the indexes of the greatest increase and greatest decrease amounts from the changes list
index_date_increase = changes.index(greatest_increase)
index_date_decrease = changes.index(greatest_decrease)

# Use the indexes from the changes list to return the dates corresponding with when the greatest increase and greatest decrease in profits occurred from the dates list
date_increase = dates[index_date_increase]
date_decrease = dates[index_date_decrease]

# Set the output path for the text file
output = Path("Outputs/output_main.txt")

# Write the resulting analysis in the output text file
with open(output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------\n")
    file.write(f"Total months: {month_count}\n")
    file.write(f"Total profit: ${total_profit}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {date_increase} ${greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: {date_decrease} ${greatest_decrease}\n")
    
# Print resulting analysis from the output_main.txt file
with open(output, 'r') as text:
    output_text_file = text.read()
    print(output_text_file)