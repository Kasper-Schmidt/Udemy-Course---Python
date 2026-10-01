available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive",
}

price_qunatity ={
    "computer": {"price": 1200, "quantity": 5},
    "monitor": {"price": 350, "quantity": 10},
    "keyboard": {"price": 200, "quantity": 12},
    "mouse": {"price": 110, "quantity": 7},
    "hdmi cable": {"price": 10, "quantity": 8},
    "dvd drive": {"price": 50, "quantity": 3},
}

current_choice = None
total_price = 0

while current_choice != "0":
    if current_choice in available_parts:
        choosen_part = available_parts[current_choice]
        if price_qunatity[choosen_part]["quantity"] > 0:
            print(f"{choosen_part} added to cart")
            price_qunatity[choosen_part]["quantity"] -= 1
            total_price += price_qunatity[choosen_part]["price"]
        else:
            print(f"{choosen_part} is out of stock.")
    else:
        print("Please add option from the list")
        for key, values in available_parts.items():
            print(f"{key}: {values}")
        print("0: to finish")

    current_choice = input("> ")

print(f"Total price: {total_price}")