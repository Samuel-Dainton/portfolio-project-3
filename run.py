# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pyfiglet import Figlet
figlet = Figlet(font="slant")
import sys
from termcolor import colored, cprint

# def main_menu()
#     Hangman
#     1 for start
#     2 for difficulty
#     3 to instructions
#     else please input a number between 1 and 3

# def difficulty()
#     Select your difficulty
#     1 for easy 10 lives
#     2 for medium 7 lives
#     3 for hard 5 lives
#     else please input a number between 1 and 3

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

# cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

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