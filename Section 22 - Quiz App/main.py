from questions import quiz

def check_answer(question_num, answer, attempt, player):
    # clear
    corrent_answer = quiz[question_num]["answer"]
    if corrent_answer.lower() == answer.lower():
        print(f"Correct answer!\n{player}'s score is {player_score[player] + 1}")
        return True
    else:
        print(f"Wrong answer!\nYou have {attempts - 1} attempts left.\nTry again...")
        return False

def switch_user(p_user_index):
    if p_user_index == 0:
        return 1
    return 0


def find_winner(player1, player2):
    if player_score[player1] > player_score[player2]:
        print(f"{player1} won the game! The score was {player_score[player1]}")
    elif player_score[player2] > player_score[player1]:
        print(f"{player2} won the game! The score was {player_score[player2]}")
    else:
        print("You are equally good, it's a tie!")



print(f"There are a total of {len(quiz)} questions, to skip a question type 'skip'")
input("Press any key to get started...")
players = input("Enter 2 player names with space between: ")
player_list = players.split(" ")
player_score = dict.fromkeys(player_list, 0)
current_player = player_list[0]

for question in quiz:
    print("----------------------------------")
    print(f"It is {current_player}'s turn")
    attempts = 2 # A player can attempt each question 2 times
    while attempts > 0:
        print(quiz[question]["question"])
        answer = input("Enter answer: ")
        if answer == "skip":
            break
        check = check_answer(question, answer, attempts, current_player)
        if check:
            player_score[current_player] += 1
            break
        attempts -= 1

    current_player_index = player_list.index(current_player)
    next_player_index = switch_user(current_player_index)
    current_player = player_list[next_player_index]

find_winner(player_list[0], player_list[1])

show_answers = input("Do you want to see the answers? y/n ").lower()
if show_answers == "y":
    for question_num, nested_dic in quiz.items():
        for key, value in nested_dic.items():
            print(f"{key}: {value}")
        print()
    print("Thanks for playing!")
else:
    quit()