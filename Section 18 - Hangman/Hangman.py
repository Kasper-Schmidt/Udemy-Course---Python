import random
import os
from hangman_stages import hangman_stages
from word_list import word_list

secret_word = random.choice(word_list)

blanks = []
for _ in range(len(secret_word)):
    blanks.append("_")

print(" ".join(blanks))

end_game = False
lives = 6
guessed_letters = [] 

while not end_game:
    guess = input("Guess a letter: ").upper()
    os.system("cls")

    if guess in guessed_letters:
        print("You have already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)

    # Gennemgå ordet og vis bogstavet på alle de rigtige positioner
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter

    if guess not in secret_word:
        lives -= 1

    if lives == 0:
        end_game = True
        print("You lose!")
        print(f"The word was: {secret_word}")

    print(" ".join(blanks))

    print(hangman_stages[lives]) # når liv er 6, printer den index 6, som er den sidste i listen

    # Hvis der ikke er flere streger, er hele ordet gættet
    if "_" not in blanks:
        end_game = True
        print("You win!")

    if end_game:
        ask = input("Do you want to play again? (Y/N)").upper()
        if ask == "Y":
            secret_word = random.choice(word_list)
            blanks.clear()
            word_length = len(secret_word)
            for _ in range(word_length):
                blanks.append("_")
            end_game = False
            guessed_letters.clear()
            lives = 6
        else:
            print("See you next time!")
        
