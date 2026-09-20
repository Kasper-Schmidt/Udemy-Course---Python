# Program to give the employee 1.5 times the hourly rate for hours worked above 40 hours. 
# Here again the program prompts the user for hours and rate per hour to compute gross pay

try:
    hours = float(input("Enter hours: "))
except ValueError:
    print("Please enter a numeric input for hours")
    quit()

try:
    rate = float(input("Enter rate: "))
except ValueError:
    print("Please enter a numeric input for rate")
    quit()


overtime = 0

if hours > 40:
    overtime = hours - 40
    
    usual_pay = 40 * rate
    
    over_pay = overtime * rate * 1.5
    
    print(f"Pay: {usual_pay + over_pay}")
    
else:
    print(f"Pay: {round(hours * rate,2)}")
    