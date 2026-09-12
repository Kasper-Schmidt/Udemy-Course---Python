# Program to give the employee 1.5 times the hourly rate for hours worked above 40 hours. 
# Here again the program prompts the user for hours and rate per hour to compute gross pay


hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))
overtime = 0

if hours > 40:
    overtime = hours - 40
    
    usual_pay = 40 * rate
    
    over_pay = overtime * rate * 1.5
    
    print(f"Pay: {usual_pay + over_pay}")
    
else:
    print(f"Pay: {round(hours * rate,2)}")
    