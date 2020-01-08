import os
import csv

onfirstrow = True
monthcount = 1
greatest_value = ["", 0]
lowest_value = ["", 0]
firstrowvalue = 0

budget_csv = os.path.join('..', '..',  'budget_data_copy.csv')
bank_output = os.path.join('bank_output.txt')

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for line in csvreader: 
       if onfirstrow:
              firstrowvalue = int(line[1])
              previous_value = int(line[1])
              total_value = firstrowvalue
              print(firstrowvalue)
              onfirstrow = False
              
              
       
       else:
            last_row_value = int(line[1])
            change_value = last_row_value - previous_value
            average_value = change_value / monthcount
            total_value += int(line[1]) 
            if change_value > greatest_value[1]:
                     greatest_value[0] = line[0]
                     greatest_value[1] = change_value
            if change_value < lowest_value[1]:
                     lowest_value[0] = line[0]
                     lowest_value[1] = change_value

       
            monthcount += 1
with open(bank_output, "w") as f:
       print("Financial Analysis", file=f)
       print("-------------------------------", file=f)
       print(f'Total Months: {monthcount}', file=f)
       print(f"Average Change: {average_value:.2f}", file=f)
       print(f'Greatest Increase in Profits: {greatest_value}', file=f)
       print(f'Greatest Decrease in Profits: {lowest_value}', file=f)

       
      
        
print(monthcount)
print(last_row_value)
print(total_value)
print(f"{average_value:.2f}")
print(greatest_value)
print(lowest_value)
