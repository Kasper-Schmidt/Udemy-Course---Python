# Divisible by 400 → leap year
# Divisible by 100, but not by 400 → not a leap year
# Divisible by 4, but not by 100 → leap year
# Otherwise → not a leap year

year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year")
    else: 
        print(f"{year} is a leap year!")

else:
    print(f"{year} is not a leap year")