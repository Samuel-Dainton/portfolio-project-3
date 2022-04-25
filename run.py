# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pyfiglet import Figlet
figlet = Figlet(font="banner3")
import pyinputplus as pyip
from termcolor import colored, cprint
from words import words_list
from man import man
import random

def main_menu():
    """
    Presents the main menu to the user
    """
    
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
    
def game():
    word = random.choice(words_list)
    hidden_word = "_ " * len(word)
    guesses = []
    life = lives
    word_guessed = False

    cprint("\nLets Play!\n", "red", attrs=["bold"])

    print(man[life])
    print(hidden_word)
    print(f"You have {life} guesses remaining!")

    while life > 0 and not word_guessed:
        guess = pyip.inputStr("Please guess a letter:").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guesses:
                print(f"You have already guessed the letter {guess}, try again.")
            elif guess not in word :
                life -= 1
                guesses.append(guess)
                print(man[life])
                print(hidden_word.upper())
                print(f"Sorry! {guess} is not in the word.")
                print(f"You have {life} guesses remaining!")
                print(f"Letters you have guessed: {guesses}")
            else:
                
                guesses.append(guess)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                  word_as_list[index] = guess
                hidden_word = "".join(word_as_list)
                if "_" not in hidden_word:
                    word_guessed = True
                print(man[life])
                print(hidden_word.upper())
                print(f"Good guess! {guess} is in the word.")
                print(f"You have {life} guesses remaining!")
                print(f"Letters you have guessed: {guesses}")

    if word_guessed:
       print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Sorry! You ran out of tries. The word  was {word}, would you like to play again?")
    
    

# def get_random_word()
#     """
#     Called when generating the game, gets a random word from a list.
#     """

# def game()
#     Good luck! You have {x} guesses to find the word. Try not to get hung!
#     print hang_man
#     print _ _ _ _ _ _ _
#     print {guessed letters}
   
#     while _ != 0 and lives > 0  What letter will you guess? input()
#     else please input a single letter or you already guessed {x}, try a different letter!
#     if _ = 0 game_win
#     else game_lose

# _______________________________________________
def main():
    main_menu()
    
    
print(figlet.renderText("HANGMAN"))
main()
