import random

def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

map_one = custom_map = [["◽️", "◽️", "◽️"],["◽️", "◽️", "◽️"],["◽️", "◽️", "◽️"]]
print_map(map_one)

golden_horizontal = random.randint(0,2)
golden_vertical = random.randint(0,2)
map_one[golden_horizontal][golden_vertical] = "⭐️"
golden_star = str(golden_horizontal + 1) + str(golden_vertical + 1)

guess = input("Where do you think the Golden Star is? (Enter row and column number, e.g. 23 for row 2 column 3): ")

if golden_star == guess:
    print("Congratulations! You found the Golden Star!")
else:
    horizontal = int(guess[0])
    vertical = int(guess[1])
    map_one[horizontal - 1][vertical - 1] = "x"

    print("Unfortunately, you did not find the Golden Star.")

print_map(map_one)
