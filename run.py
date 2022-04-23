# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pyfiglet import Figlet
figlet = Figlet(font="slant")
import sys
from termcolor import colored, cprint

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