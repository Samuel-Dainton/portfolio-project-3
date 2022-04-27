# Hangman

This is a python version of the very popular game Hangman. In this program the user is given multiple options to control the flow and difficulty of the game, with each option giving the user clear feedback on their inputs and any errors they may encounter whilst using the program.

The game first prints out the logo before taking the user to the main menu, from there they have 3 options to choose from which either lead to the game, difficulty settings or instructions. The difficulty screen allows the user to chose how many guess attempts they will have when starting the game. Both the difficulty and the instructions pages lead back to the main menu once the user is finished.
The game itself starts by presenting the user with a board space that will be used to visualise the hangman diagram as they use up more of their guesses. Underneath that are the blank spaces that will gradually fill up as the user makes correct guesses on which letters might be in the hidden word.
When the user makes an entry the program checks for multiple things that the user could have input. 
* These include:
    * Is it a letter?
    * Is it a word and ss it equal to the length of the hidden word?
    * Is it one of the key words, exit or restart?
    * Or did the user enter something else?
All of these options provide appropriate feedback to guide the user in their entries. The first two take the questions a step further to check if the users entry was correct, either one of the letters in the word or the whole word.

The game ends when either the word has been guessed or the user has run out of attempts. Once the appropriate message has been given, the user is given options to either restart, select another difficulty or quit and that loops the program back over again.

## UX

In order to make my project stand above just the code for checking words and drawing the hangman board I threw in ideas based on what I would want to see in the game as a player.

As a player I would want.
    * The ability to change the difficulty.
    * Instructions incase I hadn't read the game before.
    * Clear prompts to instruct me on how to navigate the game.
    * Options to leave the game at any point.

## Planning the Code

I began the process of building my game by imagining and writing down a walkthrough of the code which is as follows.
_______________
You need to guess a word.
The word has been selected at random.choice from a list of words.
The word needs to be represented as blank spaces so the user knows the length of the word to guess.
I can print this out as a "_" for each letter based on the len(of the word)
The user has a number of lives which are represented by the hangman graphic.
We can print a graphic that relates to the number of lives if the different graphics are indexed in a list.
When the user enters an input we need to check if it valid.
If the input is valid, is it part of the word?
If it is, we replace the corresponding blank space with the users entry.
Else we deduct the number of guesses left.
We reprint the lives, graphic, input, current guesses and feedback for their last attempt so the user doesn't have to scroll up to look for information.
Once either no more blank spaces are left in the word or lives run out the game is over.
_________________
I feel that my project ended up using this code nearly exactly as expected but with some exntensions to it over the development. I also made a flowchart to visualize the main build of the project.

![Flowchart](/images/flowchart.png)

## Third Party Libraries

After looking at a number of projects of this type, there are a few factors that seem to contribute to extra code and clutter. The first is storing large strings of ASCII graphics to be printed out in the terminal. The second is validating user input for basic interactions through the terminal. For this reason I have used the following libraries as part of my project.

* [Pyfiglet](https://github.com/pwaller/pyfiglet) - This library allows you to generate ASCII titles and text with little effort. You call the library on any piece of text and a string is returned which generates text effects when printed out to the terminal.

* [PyInputPlus](https://pypi.org/project/PyInputPlus/) - Designed to handle user input validation, this library lets you offer a number of different prompts for menus, yes/no questions, integers etc. I used this for my inputs that would only accept integer values between 1 and 3 to quickly eliminate a lot of other other incorrect inputs that a user could enter, but didn't use it for the main game where I wanted a lot of different responses for numerous types of inputs the user could make.

Other libraries used include:
* [Termcolor](https://pypi.org/project/termcolor/) allows the use of colours in text output on the terminal. This was used to highlight menu options and make the interface more visually appealing.

## Testing 

* I tested that the page works in the expected Heroku app.
* I tested that the program is responsive and adapts to look good and function on the expected terminal size of 80 characters wide and 24 rows high.
* I confirmed that all the inputs function properly and that proper feedback is given if the user inputs anything invalid.

## Bugs
### Solved Bugs

The only real struggle I ran into when making this code was trying to set the lives variable across different functions. It needed to be pre-set so that the game could start without the user needing to select the difficulty first. And it also needed to be set before the main menu so that it didn't get overrridden when going from the difficulty select back to the main menu. For this project I chose to make lives a global variable where necessary so that it could be accessed in the game function from both the preset value in the main function and the user selection in the difficulty function.

### Unsolves Bugs

When entering word and letter guesses the user can also input spaces and tabs for example (space)A or (tab)(tab)WORD(tab) and these will be accepted as valid inputs. For the purpose of this project however this does not affect anything as the game still appears to function correctly, even registering the inputs as single words or the correct length of the hidden word with or without spaces and tabs, so I'm content on not attempting to fix it.

## Validator Testing

I have tested the code and the game logic by

    * Passing the python code through the ![PEP8 validator](http://pep8online.com/) and solving any serious errors and warnings.
    * Passing invalid and valid values while testing the game to check if the program responds as expected.
    * Testing the game in gitpod terminal as well as heroku terminal.

## Future Enhancements

If I were to continue working on this project, I would probably incorporate catagories for the words. So that the user could either chose a certain catagory or use a random one, maybe even get a hint from the game to ask it what the catagory is if they're struggling to guess the word. A countdown timer would also be a fun feature to add to the difficulty of the game.

## Deployment

This game can be deployed using the Heroku app. To do so you will need to:

Create an account on Heroku
Once signed in click on the "Create New App"
Enter a name for the app and select the appropriate region
Click on create app
Go to the "Settings" tab
Click "Add Buildpack"
Add "nodejs" and then "python", the order is important here. 
Save the settings
Go to the "Deploy" tab
Select the Github option and connect to github
Search for the name of the github repository
Click on Enable Automatic Deploy for automatic deploys or Deploy Branch to manually deploy
Click "View" to view the deployed site
The deployed site can also be accessed from the Environment section in the github repository

## Credits 
### Content

I'd like to give thanks to [Afred Khan](https://github.com/afred-khan/Hangman) and his team. Whose group project helped me clarify some of the code I was going to need to build my game.

### Further Learning

[Video that demonstrates the use of PyInputPlus](https://www.youtube.com/watch?v=2201B0vGwx8)
[List of various abilities of PyFiglet](http://www.figlet.org/examples.html)
[Video that demonstrates the use of PyFiglet](https://www.youtube.com/watch?v=zUf1BM1l8MQ)
[A list of hangman words](https://www.hangmanwords.com/words)
[A simple tool for adding commas and quotes to lists of words](https://commaquote.azurewebsites.net/)
https://www.w3schools.com/python/ref_func_enumerate.asp