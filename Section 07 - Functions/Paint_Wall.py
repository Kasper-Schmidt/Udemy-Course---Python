import math

def number_of_cans(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(number_of_cans)

height = int(input("Height: "))
width = int(input("Widht: "))
coverage = int(input("Coverage: "))

number_of_cans(height, width, coverage)