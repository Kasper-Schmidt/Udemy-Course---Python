Hangman



Step 1 
    TODO 1
        Choose a random word from a given list which is word_list and assign it to a variable called secret_word

    TODO 2
        Generate/ show blanks which equals to the number of characters in secret word

    TODO 3
        Ask a player to guess a letter and assign it to a variable called guess and make it uppercase



Step 2
    TODO 1
        Check if guessed letter is already guessed or not.
        Create guessed_letters list and add guessed letters to the list and in every step check that if letter exists or not

    TODO 2
        Check if the letter that player guessed is one of the letters in the secret word

    TODO 3
        If letter is in the secret word, loop through each position in secret word and update blanks list with matched letter. 



Step 3 - Loop until player wins or lose
    TODO 1 
        By using a while loop let the okayer to guess again if the current guess is previously guessed

    TODO 2
        In the same while loop implement a logic to guess again until they have guessed all lettes and there is no blank left in the list blanks and print you win



Step 4 - Track Lives
    TODO 1
        Create lives variable and set it to 6. Check if the letter that player guessed is not one of the letters in the secret word
        If it is not, then decrease lives by one for each wrong guess
    TODO 2
        When lives reaches 0, implement a logic to stop game and print "You lose"
    TODO 3
        Instead of printing blanks list, convert it to string and print



Step 5 - ASCII Art
    TODO 1
        Add condition which ask wether player want to play again
    TODO 2
        Print ASCII Art from hangman_stages