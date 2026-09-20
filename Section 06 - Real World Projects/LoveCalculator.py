# Check both peoples names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letteres in the word LOVE occurs.
# Combine these numbers to make a 2 digit number.
# Less than 10 or greater than 85: Your score is xx, you go together like coke and mentos
# between 40 and 70: Your score is xx, you are alright together
# Otherwise: Your score is xx

your_name = input("What is your name: ")
lover_name = input("What is your lovers name: ")

combined_name = (your_name + lover_name).lower()

print(combined_name)

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("t")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

# Hvis det giver 1 og 2, i stedet for at få 3, skal jeg have 12, så jeg laver dem om til strings og tilbage til int
total = int(str(true) + str(love))

if total < 10 or total > 85:
    print(f"Your score is {total}, you go like coke and mentos")
elif 40 <= total <= 70:
    print(f"Your score is {total}, you go alright together")
else: 
    print(f"Your score is {total}, you might consider finding a new partner")