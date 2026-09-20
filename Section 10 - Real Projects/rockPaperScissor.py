import random


def select_computer_action():
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    return computer_action


def determine_winner(p_user_action, p_computer_action):
    if p_user_action == p_computer_action:
        print(f"Both players selected {p_user_action}. It's a tie!")

    elif p_user_action == "rock":
        if p_computer_action == "scissor":
            print("Rock smashes scissor, you win!")
        else:
            print("Paper covers rock! You lose.")

    elif p_user_action == "paper":
        if p_computer_action == "scissor":
            print("Scissor cuts paper, you lose!")
        else:
            print("Paper covers rock! You win!")

    elif p_user_action == "scissor":
        if p_computer_action == "paper":
            print("Scissor cuts paper! You win!")
        else:
            print("Rock smashes scissor, you lose!")


while True:
    user_action = input("Enter a choice (rock, paper, scissor): ")
    computer_action = select_computer_action()

    print(f"Computer chose: {computer_action}")

    determine_winner(user_action, computer_action)

    again = input("Would you like to play again? (y/n): ").lower()

    if again != "y":
        break