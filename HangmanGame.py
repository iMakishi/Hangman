# # # Hangman Game # # #

# Imports:

import os
import time

# BUILD Support Definitions:

def EXITCountdown(time_set): # Exit timer
    while time_set:
        mins, secs = divmod(time_set, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print("    Exiting in", timer, end = "\r")
        time.sleep(1)
        time_set -= 1
    exit

def RESTARTGame(): # Game restart feature.
    restart = input("\n    Would you like to go again? (Y/N): > ")
    if restart == "y" or restart == "Y":
        os.system("cls")
        MAINProgram()
    if restart == "n" or restart == "N":
        print("\n    Okay. Until next time.")
        time_set = 5
        EXITCountdown(int(time_set))
    if restart == "" or restart != "y" or restart != "Y" or restart != "n" or restart != "N" or restart.isdigit():
        print("\n    ERROR!")
        if restart == "":
            print("    Input is required to procede.")
        elif restart != "y" or restart != "Y" or restart != "n" or restart != "N":
            if restart.isdigit():
                print("    Input of numerical type is not accepted. Please try again.")
            else:
                print("    Input provided is not accepted. Please try again.")

        RESTARTGame()

# MAIN BUILD

def INTRO():
    print("""  _______________________________________________________________________________
                                                ______
       ________|_     |      |    /\    |\\   | |        |\\  /|    /\\    |\\   |
      |        |      |______|   /__\\   | \\  | |   ___  | \\/ |   /__\   | \\  |
    (x_x)      |      |      |  /    \\  |  \\ | |      | |    |  /    \  |  \\ |
     /|\       |      |      | /      \\ |   \\| |______| |    | /      \\ |   \\|
    / | \\      |                                                          v2.7
     / \\       |
    /   \\      |
               |
           ____|____
  _______________________________________________________________________________
""")

def MAINProgram():
    INTRO()

    prompt_word_msg = "    Mystery word: "
    mystery_word = str(input(prompt_word_msg))
    print("\033[1A" + prompt_word_msg + "\033[K")

    while mystery_word == "" or mystery_word.isdigit():
        print("\n    ERROR!")
        if mystery_word == "":
            print("    Input must be filled to procede.\n")
        if mystery_word.isdigit():
            print("    Numerical inputs are not allowed.\n")
        prompt_word_msg = "    Mystery word: "
        mystery_word = str(input(prompt_word_msg))
        print("\033[1A" + prompt_word_msg + "\033[K")
    else:
        mystery_word = mystery_word.lower()
        correctAnswer = set(mystery_word)
        correctGuess = set()

        print("\n    The mystery word contains", len(mystery_word),"letters.")
        print("\n    " + "_ " * len(mystery_word))

        num_tries = 6

        guess = str(input("\n    Make your guess: "))

        while guess == "" or guess.isdigit():
            print("\n    ERROR!")
            if guess == "":
                print("    Input must be filled to procede.\n")
            if guess.isdigit():
                print("    Numerical inputs are not allowed.\n")
            guess = str(input("    Make your guess: "))
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
                        print("""
    ________|_
    |       |
  (o_o)     |
            |
            |
            |
            |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 4:
                        print("""
    ________|_
    |       |
  (o_o)     |
    |       |
    |       |
            |
            |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 3:
                        print("""
    ________|_
    |       |
  (o_o)     |
   /|       |
  / |       |
            |
            |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 2:
                        print("""
    ________|_
    |       |
  (o_o)     |
   /|\      |
  / | \\     |
            |
            |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 1:
                        print("""
    ________|_
    |       |
  (o_o)     |
   /|\      |
  / | \\     |
   /        |
  /         |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                    if num_tries == 0:
                        print("""
    ________|_
    |       |
  (o_o)     |
   /|\      |
  / | \\     |
   / \\      |
  /   \\     |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                        print("\n    You've run out of tries.")
                    if num_tries < 0:
                        print("""
    ________|_
    |       |
  (x_x)     |
   /|\      |
  / | \\     |
   / \\      |
  /   \\     |
            |
        ____|____
    """)
                        print("\n    " + "".join(guess if guess in correctGuess else " _ " for guess in mystery_word))
                        print("\n    The word was: '" + mystery_word.title() + "'")
                        print("\n    ### GAME OVER #####")
                        break
                    print("\n    Tries left:", num_tries)

                guess = str(input("\n    Make your guess: "))
                while guess == "" or guess.isdigit():
                    print("\n    ERROR!")
                    if guess == "":
                        print("    Input must be filled to procede.\n")
                    if guess.isdigit():
                        print("    Numerical inputs are not allowed.\n")
                    guess = str(input("    Make your guess: "))

    RESTARTGame()

# EXECUTION:

MAINProgram()