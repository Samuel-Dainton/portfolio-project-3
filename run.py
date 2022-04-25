from pyfiglet import Figlet
figlet = Figlet(font="banner3")
import pyinputplus as pyip
from termcolor import colored, cprint
from words import words_list
from man import man
import random

"""
Presents the main menu to the user, allowing them to chose one of three options.
"""
def main_menu(): 
    cprint("\nWelcome to the game!\n", "red", attrs=["bold"])
    cprint("""Please chose from one of the following options...\n
    To start the game, enter 1
    To change the difficulty, enter 2
    Or to read the instructions, enter 3
    """)
    num = pyip.inputInt("Please enter an option:", min=1, max=3)
    
    if num == 1:
        game()
    if num == 2:
        difficulty()
    if num == 3:
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
        lives = 10
        diff = "Easy"
    if num == 2:
        lives = 7
        diff = "Medium"
    if num == 3:
        lives = 5
        diff = "Hard"
    
    cprint(f"\nThe difficulty has been set to {diff}...\nReturning to Main Menu", "green", attrs=["bold"])
    main_menu()

"""
Prints the instructions page to the user.
"""
def instructions():
    cprint("\nInstructions:", "red", attrs=["bold"])
    cprint("""
    In the game Hangman, you must attempt to guess a hidden word by
    entering single letters at a time.

    Each letter of the word will start out marked as an empty underlined
    spot. If you guess correctly, the letter will appear where it belongs
    in the word and once you can fill in the rest of the blanks correctly,
    you win!

    However, each time you guess an incorrect letter another part of your
    character will be added to the gallows. 
    Once you're out of guesses you will lose! So make sure to think about
    your guesses and maybe start with the letter O, as it's the most 
    common letter in the dictionary. Good luck!\n""")
    enter = input("Press enter when you're ready to return to the main menu...")
    cprint(f"\nReturning to Main Menu", "green", attrs=["bold"])
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
    print(man[life])
    print(hidden_word)
    print(f"You have {life} guesses remaining!")

    while life > 0 and not word_guessed:
        guess = pyip.inputStr("Please guess a letter:").lower()

        """Checks if the user entered one of the correct letters."""
        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                print(f"You have already guessed the letter {guess}, try again.")
            elif guess not in word:
                life -= 1
                guesses.append(guess.upper())
                print(man[life])
                print(hidden_word.upper())
                print(f"Sorry! {guess.upper()} is not in the word.")
                print(f"You have {life} guesses remaining.")
                print(f"Letters you have guessed: {sorted(guesses)}")
            else:
                guesses.append(guess.upper())

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

                print(man[life])
                print(hidden_word.upper())
                print(f"Good guess! {guess.upper()} is in the word.\n")
                print(f"You have {life} guesses remaining.")
                print(f"Letters you have guessed: {guesses}\n")
        
            """Checks if the user entered the correct word."""
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You have already guessed the word {guess}")
            elif guess != word:
                life -= 1
                guessed_words.append(guess.upper())
                print(man[life])
                print(hidden_word.upper())
                print(f"Sorry! {guess.upper()} is not the word.\n")
                print(f"You have {life} guesses remaining!")
                print(f"Letters you have guessed: {sorted(guesses)}")
                print(f"Words you have guessed: {guessed_words}\n")
            else:
                word_guessed = True
                
            """Triggers when the user wants to exit or restart the game."""
        elif guess == "exit":
            main_menu()
        elif guess == "restart":
            game()

        else:
            cprint(f"\nSorry! You entered {guess}, please enter either a letter or a single word.\n", "red", attrs=["bold"])
    
    """Prints a message and triggers the restart function if the game is won, else if the game is lost."""
    if word_guessed:
        print(man[life])
        print(word.upper())
        cprint("Congratulations! You guessed the word correctly.", "green", attrs=["bold"])
        restart()
    else:
        print(man[life])
        print(hidden_word.upper())
        cprint(f"Sorry! You ran out of tries. The word was, {word}.", "red", attrs=["bold"])
        restart()

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
