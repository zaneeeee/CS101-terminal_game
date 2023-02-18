"""Who Wants to Be a Millionaire terminal game.
A command-line version of the game show "Who Wants to Be a Millionaire".

This program allows the user to play a trivia game, where they are asked a series of questions
with four possible answers, and must choose the correct one to advance to the next level. The
game ends when the player either wins the grand prize of 1 million points, or answers a question
incorrectly.

The program reads the questions from a separate module called "questions.py", which contains a
list of dictionaries representing each question. Each dictionary has the following keys:
- 'question': a string representing the question
- 'options': a list of strings representing the possible answer options
- 'answer': a string representing the answer
"""
import random
from questions import QUESTIONS

# Define constant variables
ANSWER_OPTIONS = ['a', 'b', 'c', 'd']
POINTS = [100, 1000, 10000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 1000000]
BANNER = """
WHO WANTS TO BE A...

███╗   ███╗██╗██╗     ██╗     ██╗ ██████╗ ███╗   ██╗ █████╗ ██╗██████╗ ███████╗██████╗ 
████╗ ████║██║██║     ██║     ██║██╔═══██╗████╗  ██║██╔══██╗██║██╔══██╗██╔════╝╚════██╗
██╔████╔██║██║██║     ██║     ██║██║   ██║██╔██╗ ██║███████║██║██████╔╝█████╗    ▄███╔╝
██║╚██╔╝██║██║██║     ██║     ██║██║   ██║██║╚██╗██║██╔══██║██║██╔══██╗██╔══╝    ▀▀══╝ 
██║ ╚═╝ ██║██║███████╗███████╗██║╚██████╔╝██║ ╚████║██║  ██║██║██║  ██║███████╗  ██╗   
╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝  ╚═╝
    """

class Player:
    """
    Represents a player with a name and score.

    Attributes:
    - name (str): the player's name
    - score (int): the player's current score

    Methods:
    - update_score(index): updates the player's score based on the given index,
      which is used to retrieve the point value from the constant POINTS list
    """
    def __init__(self, name):
        """Initializes a new Player object with the given name and a score of 0"""
        self.name = name
        self.score = 0

    def __repr__(self):
        """Return a string representation of the player's score"""
        return f"{self.name}, your score is {self.score}"

    def update_score(self, index):
        """Updates the player's score based on the given index"""
        self.score = POINTS[index]

def get_user_input(valid_input):
    """Get user input and check if it's valid"""
    while True:
        user_input = input("Enter your choice: ")
        if user_input in valid_input:
            return user_input
        else: #If the input is invalid, print an error message.
            print("Invalid input. Please enter a, b, c, or d.")

def game_over():
    """Prompt the player to either restart or quit the game"""
    choice = input("Would you like to restart the game (r) or quit (q)?: ").lower()
    if choice == 'r':
        return play() #restart
    elif choice == 'q':
        return exit() #quit
    else: #If the input is invalid, print an error message.
        print("Invalid input. Please enter 'r' to restart or 'q' to quit.")

def play():
    """Main method to run game"""
    questions = QUESTIONS
    random.shuffle(questions) #randomize the order of questions
    print(BANNER) #print ascii art
    player_name = input("Please enter your name: ") #get the player's name
    player = Player(player_name) #instantiate the player object
    print(f"\nWelcome to WWTBAM {player.name}!") #welcome message for game

    # Loop through questions list
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}:") #print the question number
        print(f"{question['question']}") #print the question

        # Randomise the order of options
        options = question['options']
        random.shuffle(options)
        for j, option in enumerate(options):
            print(f"{ANSWER_OPTIONS[j]}. {option}") #print the options

        answer = get_user_input(ANSWER_OPTIONS) #get user input

        # If the answer is correct, update the player's score and print "Correct!"
        if answer == chr(97 + options.index(question['answer'])).lower():
            print("\nCorrect!")
            player.update_score(index)
        else:
            # If the answer is incorrect, print "Incorrect!"
            print("\nIncorrect!")
            print(f"Thanks for playing {repr(player)}")
            game_over()

        # Print player's current score
        print(repr(player))

    # Print the final score after all questions have been answered
    print(f"Thanks for playing {repr(player)}")
    game_over()

play()
