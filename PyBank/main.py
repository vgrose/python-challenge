#Import necessary:
import os
import csv

#Set file location:
csvpath= os.path.join("budget_data.csv")

#Open file
with open(csvpath) as csvfile:

    #Separate each column at comma:
    budget_data = csv.reader(csvfile, delimiter=',')

    #Skip header:
    csv_header = next(budget_data)

    #Set initial values to zero:
    total_months=0
    net_total=0
    greatest_increase=0
    greatest_decrease=0

    #Iterate through rows in imported csv file:
    for row in budget_data:

        #Add up the total months:
        total_months=total_months+1

        #Name variables:
        profit=int(row[1])
        month=row[0]

        #Add up the total profits:
        net_total=net_total+profit

        #Set initial profit:
        if total_months==1:
            initial_profit=profit

        #Find the greatest profit increase:
        if profit>greatest_increase:
            greatest_increase=profit
            greatest_increase_month=month

        #Find greatest profit decrease:
        if profit<greatest_decrease:
            greatest_decrease=profit
            greatest_decrease_month=month

        #Set final profit:
        final_profit=profit

    #Calculate average profit:
    average_profit=(final_profit-initial_profit)/(total_months-1)

    #Format average profit like moneys:
    average=round(average_profit,2)

    #Print results:
    print("")
    print("Financial Analyis")
    print("")
    print("---------------------------------")
    print("")
    print(f"Total Months: {total_months}")
    print("")
    print(f"Total: ${net_total}")
    print("")
    print(f"Average Change: ${average}")
    print("")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print("")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    print("")
    print("---------------------------------")
    print("")

    #Print results to text file and close:         
    text_file = open("PyBank_Output.txt", "w")
    text_file.writelines(["Financial Analyis \n","-------------- \n",
        f"Total Months: {total_months} \n", f"Total: ${net_total} \n", 
            f"Average Change: ${average} \n", 
                f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n", 
                    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) \n",
                        "--------------"  ])
    text_file.close()