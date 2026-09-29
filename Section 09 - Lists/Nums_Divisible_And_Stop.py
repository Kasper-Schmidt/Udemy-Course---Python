list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]


def numbers_divisible_by_five(p_list):
    for num in p_list:
        if num > 130:
            print("STOP")
            break

        if num % 5 == 0:
            print(num)


numbers_divisible_by_five(list1)