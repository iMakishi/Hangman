# Imports:

import os, sys, time, datetime

from gameArt import titleIntro
from gameArt import sentenceProgression

from gameText import aboutText
from gameText import helpText

# Parameters:

exclusiveWords = ["exit", "help", "about"]
prohibitedWords = ["fuck", "fucker", "cunt", "pussy", "kike", "dago", "wog", "arsehole", "asshole"] # Don't research all existing words cause it's deppresing to read their definitions.

# Side Functions:

def gameIntro():
    print(titleIntro)

def EXITCountdown(x): # Exit program timer
    print("\n")
    total_seconds = x
    while total_seconds > -1:
        timer = datetime.timedelta(seconds = total_seconds)
        print("Exiting in", timer, end = '\r')
        time.sleep(1)
        total_seconds -= 1
    sys.exit()

def RESTART(): # Restart feature.
    restart = input("\n" + "Would you like to go again? (Y/N): > ")
    if restart == "y" or restart == "Y":
        os.system('cls')
        game() # Main Function | Change this line when using this function in other scripts.
    if restart == "n" or restart == "N":
        print("\n" + "Okay. Until next time!")
        timer = 5
        EXITCountdown(int(timer))
    if restart == "" or restart != "y" or restart != "Y" or restart != "n" or restart != "N" or restart.isdigit():
        if restart == "":
            print("\n" + "Input is required to procede.")
        elif restart != "y" or restart != "Y" or restart != "n" or restart != "N":
            if restart.isdigit():
                print("\n" + "Input of numerical type is not accepted." + "\n" + "Please try again.")
            else:
                print("\n" + "Input provided is not accepted." + "\n" + "Please try again.")

        RESTART()

# ----- Game Logic ----- #

def game():
    gameIntro()

    prompt_word_msg = "Mystery word: "
    mystery_word = str(input(prompt_word_msg))
    print('\033[1A' + prompt_word_msg + '\033[K')
    mystery_word = mystery_word.lower()

    while mystery_word == "" or mystery_word.isdigit() or mystery_word in exclusiveWords or mystery_word in prohibitedWords:
        if mystery_word == "":
            print("\n" + "# # # ERROR: Input must be filled to procede. # # #" + "\n")
        if mystery_word.isdigit():
            print("\n" + "# # # ERROR: Numerical inputs are not allowed. # # #" + "\n")
        if mystery_word in exclusiveWords:
            if mystery_word == exclusiveWords[0]:
                timer = 5
                EXITCountdown(int(timer))
            if mystery_word == exclusiveWords[1]:
                print(helpText)
            if mystery_word == exclusiveWords[2]:
                print(aboutText)
        if mystery_word in prohibitedWords:
            print("\n" + "# # # ERROR: PROHIBITED WORD # # #" + "\n")

        prompt_word_msg = "Mystery word: "
        mystery_word = str(input(prompt_word_msg))
        print('\033[1A' + prompt_word_msg + '\033[K')
        mystery_word = mystery_word.lower()
    else:
        correctAnswer = set(mystery_word)
        correctGuess = set()

        print("_" * 50 + ("\n" * 2))

        print("The mystery word contains", len(mystery_word),"letters.")
        print("_ " * len(mystery_word))

        print("\n" + "_" * 50 + "\n")

        num_tries = 6

        guess = str(input("Make your guess: "))
        guess = guess.lower()

        while guess == "" or guess.isdigit() or guess in exclusiveWords:
            if guess == "":
                print("\n" + "# # # ERROR: Input must be filled to procede. # # #" + "\n")
            if guess.isdigit():
                print("\n" + "# # # ERROR: Numerical inputs are not allowed. # # #" + "\n")
            if guess in exclusiveWords:
                if guess == "about":
                    print(aboutText)
                if guess == "help":
                    print(helpText)
                if guess == "exit":
                    timer = 5
                    EXITCountdown(int(timer))

            guess = str(input("Make your guess: "))
            guess = guess.lower()
        else:
            while guess != "":
                if guess == mystery_word:
                    print("\n" + "\033[4m" + "Correct!" + "\033[0m")
                    print(("_" * 50) + ("\n" * 2) + "# # # \033[4mYOU'VE WON!\033[0m # # #")
                    print("\n" + "The mystery word was indeed '" + mystery_word.title() + "'" + "\n" + ("_" * 50))
                    break
                elif guess in mystery_word:
                    print("\n" + "\033[4m" + "Correct!" + "\033[0m")
                    correctGuess.add(guess)
                    if correctGuess == correctAnswer:
                        print(("_" * 50) + ("\n" * 2) + "# # # \033[4mYOU'VE WON!\033[0m # # #")
                        print("\n" + "The mystery word was indeed '" + mystery_word.title() + "'" + "\n" + ("_" * 50))
                        break
                    print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                else:
                    print("\n" + "\033[4m" + "Incorrect!" + "\033[0m")
                    num_tries = num_tries - 1
                    if num_tries == 5:
                        print(sentenceProgression[0])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 4:
                        print(sentenceProgression[1])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 3:
                        print(sentenceProgression[2])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 2:
                        print(sentenceProgression[3])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 1:
                        print(sentenceProgression[4])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 0:
                        print(sentenceProgression[5])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                        print("\n" + "Beware! You've run out of tries.")
                    if num_tries < 0:
                        print(sentenceProgression[6])
                        print("\n" + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                        print(("_" * 50) + ("\n" * 2) + "The word was: '" + mystery_word.title() + "'")
                        print("\n" + "# # # \033[4mGAME OVER\033[0m # # #" + "\n" + ("_" * 50))
                        break
                    print("\n" + "Tries left:", num_tries)

                guess = str(input("\n" + "Make your guess: "))
                guess = guess.lower()

                while guess == "" or guess.isdigit() or guess in exclusiveWords:
                    if guess == "":
                        print("\n" + "# # # ERROR: Input must be filled to procede. # # #" + "\n")
                    if guess.isdigit():
                        print("\n" + "# # # ERROR: Numerical inputs are not allowed. # # #" + "\n")
                    if guess in exclusiveWords:
                        if guess == "about":
                            print(aboutText)
                        if guess == "help":
                            print(helpText)
                        if guess == "exit":
                            timer = 5
                            EXITCountdown(int(timer))

                    guess = str(input("Make your guess: "))
                    guess = guess.lower()

    RESTART()

# ------------------------- Logic Execution ------------------------- #

if __name__ == '__main__':
    game()