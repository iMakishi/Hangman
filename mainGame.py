# Imports:

import os, sys, time, datetime

from gameArt import titleIntro
from gameArt import sentenceProgression

from gameText import aboutText
from gameText import helpText

# Parameters:

exclusiveWords = ["about", "help", "exit"]

# Side Functions:

def gameIntro():
    print(titleIntro)

def EXITCountdown(x): # Exit program timer
    total_seconds = x
    while total_seconds > -1:
        timer = datetime.timedelta(seconds = total_seconds)
        print("    Exiting in", timer, end = '\r')
        time.sleep(1)
        total_seconds -= 1
    sys.exit()

def RESTART(): # Restart feature.
    restart = input("\n    Would you like to go again? (Y/N): > ")
    if restart == "y" or restart == "Y":
        os.system('cls')
        game() # Main Function | Change this line when using this function in other scripts.
    if restart == "n" or restart == "N":
        print("\n    Okay. Until next time!")
        timer = 5
        EXITCountdown(int(timer))
    if restart == "" or restart != "y" or restart != "Y" or restart != "n" or restart != "N" or restart.isdigit():
        if restart == "":
            print("    Input is required to procede.")
        elif restart != "y" or restart != "Y" or restart != "n" or restart != "N":
            if restart.isdigit():
                print("    Input of numerical type is not accepted. Please try again.")
            else:
                print("    Input provided is not accepted. Please try again.")

        RESTART()

# ----- Game Logic ----- #

def game():
    gameIntro()

    prompt_word_msg = "    Mystery word: "
    mystery_word = str(input(prompt_word_msg))
    print('\033[1A' + prompt_word_msg + '\033[K')
    mystery_word = mystery_word.lower()

    while mystery_word == "" or mystery_word.isdigit():
        if mystery_word == "":
            print("    Input must be filled to procede.\n")
        if mystery_word.isdigit():
            print("    Numerical inputs are not allowed.\n")
        prompt_word_msg = "    Mystery word: "
        mystery_word = str(input(prompt_word_msg))
        print('\033[1A' + prompt_word_msg + '\033[K')
        mystery_word = mystery_word.lower()
    else:
        while mystery_word in exclusiveWords:
            if mystery_word in exclusiveWords:
                if mystery_word == "about":
                    print(aboutText)
                if mystery_word == "help":
                    print(helpText)
                if mystery_word == "exit":
                    timer = 5
                    EXITCountdown(int(timer))
            prompt_word_msg = "    Mystery word: "
            mystery_word = str(input(prompt_word_msg))
            print('\033[1A' + prompt_word_msg + '\033[K')
            mystery_word = mystery_word.lower()
        else:
            correctAnswer = set(mystery_word)
            correctGuess = set()

            print("\n    The mystery word contains", len(mystery_word),"letters.")
            print("\n    " + "_ " * len(mystery_word))

            num_tries = 6

            guess = str(input("\n    Make your guess: "))
            guess = guess.lower()

            while guess == "" or guess.isdigit():
                if guess == "":
                    print("    Input must be filled to procede.\n")
                if guess.isdigit():
                    print("    Numerical inputs are not allowed.\n")
                guess = str(input("    Make your guess: "))
                guess = guess.lower()
            else:
                while guess in exclusiveWords:
                    if guess in exclusiveWords:
                        if guess == "about":
                            print(aboutText)
                        if guess == "help":
                            print(helpText)
                        if guess == "exit":
                            timer = 5
                            EXITCountdown(int(timer))

                    guess = str(input("\n    Make your guess: "))
                    guess = guess.lower()
                else:
                    while guess != "":
                        if guess == mystery_word:
                            print("\n    Correct")
                            print("\n    You've won!")
                            print("    The mystery word was indeed '" + mystery_word.title() + "'")
                            break
                        elif guess in mystery_word:
                            print("\n    Correct!")
                            correctGuess.add(guess)
                            if correctGuess == correctAnswer:
                                print("\n    You've won!")
                                print("    The mystery word was indeed '" + mystery_word.title() + "'")
                                break
                            print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                        else:
                            print("\n    Incorrect!")
                            num_tries = num_tries - 1
                            if num_tries == 5:
                                print(sentenceProgression[0])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                            if num_tries == 4:
                                print(sentenceProgression[1])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                            if num_tries == 3:
                                print(sentenceProgression[2])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                            if num_tries == 2:
                                print(sentenceProgression[3])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                            if num_tries == 1:
                                print(sentenceProgression[4])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                            if num_tries == 0:
                                print(sentenceProgression[5])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                                print("\n    Beware! You've run out of tries.")
                            if num_tries < 0:
                                print(sentenceProgression[6])
                                print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                                print("\n    The word was: '" + mystery_word.title() + "'")
                                print("\n    ### GAME OVER #####")
                                break
                            print("\n    Tries left:", num_tries)

                        guess = str(input("\n    Make your guess: "))
                        guess = guess.lower()

                        while guess == "" or guess.isdigit():
                            if guess == "":
                                print("    Input must be filled to procede.\n")
                            if guess.isdigit():
                                print("    Numerical inputs are not allowed.\n")
                            guess = str(input("    Make your guess: "))
                            guess = guess.lower()
                        else:
                            while guess in exclusiveWords:
                                if guess in exclusiveWords:
                                    if guess == "about":
                                        print(aboutText)
                                    if guess == "help":
                                        print(helpText)
                                    if guess == "exit":
                                        timer = 5
                                        EXITCountdown(int(timer))

                                    guess = str(input("    Make your guess: "))
                                    guess = guess.lower()

                                    while guess == "" or guess.isdigit():
                                        if guess == "":
                                            print("    Input must be filled to procede.\n")
                                        if guess.isdigit():
                                            print("    Numerical inputs are not allowed.\n")
                                        guess = str(input("    Make your guess: "))
                                        guess = guess.lower()

    RESTART()

# ----- Logic Execution ----- #
if __name__ == '__main__':
    game()