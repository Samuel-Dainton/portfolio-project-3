# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pyfiglet import Figlet
figlet = Figlet(font="banner3")
import pyinputplus as pyip
from termcolor import colored, cprint

def main_menu():
    """
    Presents the main menu to the user
    """
    
    cprint("Welcome to the game!\n", "red", attrs=["bold"])
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
    cprint("Select your difficulty!\n", "red", attrs=["bold"])
    cprint("""Please chose from one of the following options...\n
    For Easy (10 Lives), enter 1
    For Medium (7 Lives), enter 2
    Or for Hard (5 Lives), enter 3
    """)
    num = pyip.inputInt("Please enter an option:", min=1, max=3)
    
    if num == 1:
        lives = 10
    if num == 2:
        lives = 7
    if num == 3:
        lives = 51
    main_menu()

# def instructions()
#     how to play:
#     alfa bravo charlie

# def get_random_word()
#     """
#     Called when generating the game, gets a random word from a class list.
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

# print(figlet.renderText("Hello World!"))

# cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)

# print("""
#         ___________
#         | /       |
#         ||        O
#         ||       /|\\
#         ||________|____
#         ||       / \\   /|
#         | \\           /
#         L____________/
#         ||          ||
#         """)

print(figlet.renderText("HANGMAN"))
main_menu()