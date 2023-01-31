# Who wants to be a millionaire terminal game
import random

# Class to store player information such as name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    # Method to update player's score
    def update_score(self, score):
        self.score += score

# Define questions, options, answers
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'What is the currency of Japan?',
        'options': ['Yen', 'Dollar', 'Euro', 'Pound'],
        'answer': 'Yen'
    },
    {
        'question': 'What is the tallest mountain in the world?',
        'options': ['Mount Kilimanjaro', 'Mount Everest', 'K2', 'Mount Blanc'],
        'answer': 'Mount Everest'
    },
    {
        'question': 'What is the largest ocean in the world?',
        'options': ['Indian Ocean', 'Atlantic Ocean', 'Arctic Ocean', 'Pacific Ocean'],
        'answer': 'Pacific Ocean'
    }
]

# Class to handle the game
class Game:
    def __init__(self):
        self.questions = questions

    # Title for the game
    def title(self):
        print("""
WHO WANTS TO BE A...
  __  __ _____ _      _      _____ ____  _   _          _____  ______ ___  
 |  \/  |_   _| |    | |    |_   _/ __ \| \ | |   /\   |  __ \|  ____|__ \ 
 | \  / | | | | |    | |      | || |  | |  \| |  /  \  | |__) | |__     ) |
 | |\/| | | | | |    | |      | || |  | | . ` | / /\ \ |  _  /|  __|   / / 
 | |  | |_| |_| |____| |____ _| || |__| | |\  |/ ____ \| | \ \| |____ |_|  
 |_|  |_|_____|______|______|_____\____/|_| \_/_/    \_\_|  \_\______|(_)  

        """)

    # Game over method: quit or restart
    def game_over(self, player):
        print(f"\nThanks for playing WWTBAM, {player.name}. Better luck next time!")
        while True:
            choice = input("Would you like to restart the game (r) or quit (q)?: ").lower()
            if choice == 'r':
                return True
            elif choice == 'q':
                return False
            else:
                print("Invalid input. Please enter 'r' to restart or 'q' to quit.")

    # Main method to run game
    def play(self):
        random.shuffle(self.questions) #randomize the order of questions
        self.title() #print title
        player_name = input("Please enter your name: ") #get the player's name
        player = Player(player_name) #instantiate the player object
        print(f"\nWelcome to WWTBAM {player.name}!") #welcome message for game
        current_score = 0

        # Loop through questions list
        for index, question in enumerate(self.questions):
            print()
            print(f"Question {index + 1}:") #print the question number
            print(f"{question['question']}") #print the question

            # Randomise the order of options
            options = question['options']
            random.shuffle(options)
            for j, option in enumerate(options):
                print(f"{chr(97 + j).lower()}. {option}") #print the options

            # Check to ensure the player's input is 'a', 'b', 'c', or 'd'
            while True:
                answer = input("Your answer: ").lower()
                if answer in ["a", "b", "c", "d"]:
                    break
                else:
                    print("Invalid input. Please enter a valid answer (a, b, c, or d)")

            # If the answer is correct, update the player's score and print "Correct!"
            if answer == chr(97 + options.index(question['answer'])).lower():
                print("\nCorrect!")
                current_score += (index + 1) * 100
                player.update_score(current_score)
            else:
                # If the answer is incorrect, print "Incorrect!"
                print("\nIncorrect!")
                if self.game_over(player):
                    return self.play() #restart game
                else:
                    exit() #quit game

            # Print player's current score
            print(f"\nCurrent score: {player.score}")

        # Print the final score after all questions have been answered
        print(f"Thanks for playing, {player.name}! Your final score is {player.score}")

game = Game()
game.play()
