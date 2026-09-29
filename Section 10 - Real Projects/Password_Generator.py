import random

letters = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

number_of_letters = input("How many letters do you want in your password? ")
number_of_nums = input("How many numbers do you want in your password? ")
number_of_symbol = input("How many symbols do you want in your password? ")

number_of_letters = int(number_of_letters)
number_of_nums = int(number_of_nums)
number_of_symbol = int(number_of_symbol)

password = ""

for letter in range(1, number_of_letters + 1):
    password += random.choice(letters)

for num in range(1, number_of_nums + 1):
    password += random.choice(nums)

for symbol in range(1, number_of_symbol + 1):
    password += random.choice(symbols)

print(f"Your password is: {password}")

password_list = list(password)
random.shuffle(password_list)

advanced_password = ""
for apc in password_list:
    advanced_password += apc

print(f"Your advanced password is: {advanced_password}")