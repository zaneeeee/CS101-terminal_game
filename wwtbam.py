"""Who Wants to Be a Millionaire terminal game.
This module implements a simple terminal-based version of the game "Who Wants to Be a Millionaire".
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

# Class to handle the game
class Game:
    def __init__(self):
        self.questions = QUESTIONS

    # Game over method: quit or restart
    def game_over(self):
        choice = input("Would you like to restart the game (r) or quit (q)?: ").lower()
        if choice == 'r':
            return self.play()
        elif choice == 'q':
            return exit()
        else:
            print("Invalid input. Please enter 'r' to restart or 'q' to quit.")

    # Get user input method
    def get_user_input(self, valid_input):
        while True:
            user_input = input("Enter your choice: ")
            # Check to ensure the player's input is valid
            if user_input in valid_input:
                return user_input
            else:
                print("Invalid input. Please enter a, b, c, or d.")

    # Main method to run game
    def play(self):
        random.shuffle(self.questions) #randomize the order of questions
        print(BANNER)
        player_name = input("Please enter your name: ") #get the player's name
        player = Player(player_name) #instantiate the player object
        print(f"\nWelcome to WWTBAM {player.name}!") #welcome message for game

        # Loop through questions list
        for index, question in enumerate(self.questions):
            print(f"\nQuestion {index + 1}:") #print the question number
            print(f"{question['question']}") #print the question

            # Randomise the order of options
            options = question['options']
            random.shuffle(options)
            for j, option in enumerate(options):
                print(f"{ANSWER_OPTIONS[j]}. {option}") #print the options

            answer = self.get_user_input(ANSWER_OPTIONS) #get user input

            # If the answer is correct, update the player's score and print "Correct!"
            if answer == chr(97 + options.index(question['answer'])).lower():
                print("\nCorrect!")
                player.update_score(index)
            else:
                # If the answer is incorrect, print "Incorrect!"
                print("\nIncorrect!")
                print("Thanks for playing " + repr(player))
                self.game_over()

            # Print player's current score
            print(repr(player))

        # Print the final score after all questions have been answered
        print("Thanks for playing " + repr(player))
        self.game_over()

game = Game()
game.play()
