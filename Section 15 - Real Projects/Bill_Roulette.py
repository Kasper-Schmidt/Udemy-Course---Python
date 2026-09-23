import random 

names_string = input("Input everyone's name, seperated by comma: ")
list_people = names_string.split(", ")

buyer = random.choice(list_people) 

print(f"{buyer} is going to pay for all today!")





'''
import random 

names_string = input("Input everyone's name, seperated by comma: ")
list_people = names_string.split(", ")

num_items = len(list_people)

random_int = random.randint(0, num_items - 1)

person_name = names[random_int]

print(f"{person_name} is going to pay for all today!")

'''