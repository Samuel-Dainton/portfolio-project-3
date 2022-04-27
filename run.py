from pyfiglet import Figlet
import pyinputplus as pyip
from termcolor import colored, cprint
from words import words_list
from man import man
import random
figlet = Figlet(font="banner3")

"""
Presents the main menu to the user, allowing them to chose one of three options.
"""
def main_menu():
    cprint("Welcome to the game!\n", "red", attrs=["bold"])
    cprint("""Please chose from one of the following options...\n
    To start the game, enter 1
    To change the difficulty, enter 2
    Or to read the instructions, enter 3
    """)
    num = pyip.inputInt("Please enter an option:", min=1, max=3)
    if num == 1:
        cprint(f"\nLoading the game...", "green", attrs=["bold"])
        game()
    if num == 2:
        cprint(f"\nLoading difficulty options...", "green", attrs=["bold"])
        difficulty()
    if num == 3:
        cprint(f"\nLoading instructions page...", "green", attrs=["bold"])
        instructions()

"""
Allows the user to select one of three difficulty options before returning them to the main menu.
"""
def difficulty():
    cprint("\nSelect your difficulty!\n", "red", attrs=["bold"])
    cprint("""Please chose from one of the following options...\n
    For Easy (10 Lives), enter 1
    For Medium (7 Lives), enter 2
    Or for Hard (5 Lives), enter 3
    """)
    num = pyip.inputInt("Please enter an option:", min=1, max=3)
    
    global lives
    if num == 1:
        lives = 12
        diff = "Easy"
    if num == 2:
        lives = 10
        diff = "Medium"
    if num == 3:
        lives = 7
        diff = "Hard"
    
    cprint(f"\nThe difficulty has been set to {diff}.\nReturning to Main Menu...\n", "green", attrs=["bold"])
    main_menu()

"""
Prints the instructions page to the user.
"""
def instructions():
    cprint("\nInstructions:", "red", attrs=["bold"])
    cprint("""
    In the game Hangman, you must attempt to guess a hidden word by
    entering single letters that you think might be in the word, or
    the whole word.

    Each letter of the word will start out marked as an empty underlined
    spot. If you guess a letter correctly, the letter will appear where 
    it belongs in the word and once you can fill in the rest of the blanks
    correctly or guess the whole word, you win!

    However, each time you guess an incorrect letter another part of your
    character will be added to the gallows. Guessing a whole word only
    reduces your attempts by 1, so it could be usefull in eliminating
    a number of letters at once.

    Once you're out of guesses, you will lose! So make sure to think about
    your guesses. Good luck!\n""")
    enter = input("Press enter when you're ready to return to the main menu...")
    cprint(f"\nReturning to Main Menu...\n", "green", attrs=["bold"])
    main_menu()

"""
Starts by getting a random word from the words_list in the words file and runs the main game.
"""    
def game():
    word = random.choice(words_list)
    hidden_word = "_" * len(word)
    guesses = []
    guessed_words = []
    life = lives
    word_guessed = False

    cprint("\nLets Play!\n", "red", attrs=["bold"])
    cprint("If you want to quit at any point, you can enter 'exit' to go to the main menu.", "green", attrs=["bold"])
    cprint("Or 'restart' to restart the game with a new word.", "green", attrs=["bold"])
    
    """Used to print the games display."""
    def print_game():
        print(man[life])
        print(f"The word is: {hidden_word}")
        print(f"\nYou have {life} guesses remaining.")
        if guesses:
            print(f"Letters you have guessed: {sorted(guesses)}")
        if guessed_words:
            print(f"Words you have guessed: {guessed_words}")

    print_game()

    while life > 0 and not word_guessed:
        guess = pyip.inputStr("Please guess a letter or a word:").upper()

        """Checks if the user entered one of the correct letters."""
        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                cprint(f"You have already guessed the letter {guess}, try again.", "red", attrs=["bold"])
            elif guess not in word:
                life -= 1
                guesses.append(guess)
                print_game()
                cprint(f"Sorry! {guess} is not in the word.", "green", attrs=["bold"])
            else:
                guesses.append(guess)

                """Turns the hidden_word into a list using indexing and list comprehension."""
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                """Replaces the corresponding _ with the guessed letter."""
                for index in indices:
                    word_as_list[index] = guess
                    hidden_word = "".join(word_as_list)

                """Checks to see if the word has been guessed once no _ remain."""
                if "_" not in hidden_word:
                    word_guessed = True

                print_game()
                cprint(f"Good guess! {guess} is in the word.", "green", attrs=["bold"])
        
            """Checks if the user entered the correct word."""
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                cprint(f"You have already guessed the word {guess}", "red", attrs=["bold"])
            elif guess != word:
                life -= 1
                guessed_words.append(guess)
                print_game()
                cprint(f"Sorry! {guess} is not the word.", "green", attrs=["bold"])
            else:
                word_guessed = True
                
            """Triggers when the user wants to exit or restart the game."""
        elif guess == "EXIT":
            main_menu()
        elif guess == "RESTART":
            game()
        elif len(guess) >1 and guess is not len(word):
            cprint(f"\nSorry! You entered {guess} which isn't the same length as the word you need to guess.\n", "red", attrs=["bold"])
        else:
            cprint(f"\nSorry! You entered {guess}, please enter either a letter or a single word.\n", "red", attrs=["bold"])
    
    """Prints a message and triggers the restart function if the game is won, else if the game is lost."""
    if word_guessed:
        print(man[life])
        print(word)
        cprint(f"\nCongratulations! You guessed the word {word} correctly.", "green", attrs=["bold"])
        restart()
    else:
        print(man[life])
        print(hidden_word)
        cprint(f"Sorry! You ran out of tries. The word was, {word}.", "red", attrs=["bold"])
        restart()

def print_game():
    pass

"""
Prompted when the game is won or lost to let the user decide what they would like to do next.
"""
def restart():
    cprint("""\nWould you like to play again?\n
    To re-start the game, enter 1
    To go to the difficulty selection, enter 2
    Or to quit to the menu, enter 3
    """)

    num = pyip.inputInt("Please enter an option:", min=1, max=3)
    
    if num == 1:
        game()
    if num == 2:
        difficulty()
    if num == 3:
        main_menu()

def main():
    global lives
    lives = 7
    main_menu()
    
print(figlet.renderText("HANGMAN"))
main()