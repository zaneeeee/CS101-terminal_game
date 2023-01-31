# Who wants to be a millionaire terminal game
import random

# Class to store player information such as name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    # Method to update player's score
    def update_score(self, score):
        self.score = score

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

question_value = [500, 1000, 2000, 5000, 10000, 20000, 50000, 75000, 1500000, 200000, 500000, 1000000]

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

    # Main method to run game
    def play(self):
        random.shuffle(self.questions) #randomize the order of questions
        self.title() #print title
        player_name = input("Please enter your name: ") #get the player's name
        player = Player(player_name) #instantiate the player object
        print(f"\nWelcome to WWTBAM {player.name}!") #welcome message for game

        # Loop through questions list
        for index, question in enumerate(self.questions):
            print()
            print(f"Question {index + 1}:") #print the question number
            print(f"{question['question']}") #print the question

            # Randomise the order of options
            self.options = question['options']
            random.shuffle(self.options)
            for j, option in enumerate(self.options):
                print(f"{chr(97 + j).upper()}. {option}") #print the options

            # Check to ensure the player's input is 'A', 'B', 'C', or 'D'
            while True:
                self.answer = input("Your answer: ").upper()
                if self.answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid input. Please enter a valid answer (A, B, C, or D)")

            # If the answer is correct, update the player's score and print "Correct!"
            if self.answer == chr(97 + self.options.index(question['answer'])).upper():
                print("\nCorrect!") 
                player.update_score(question_value[index])
            else:
                # If the answer is incorrect, print "Incorrect!" and an exit message
                print("\nIncorrect!")
                print(f"\nThanks for playing WWTBAM, {player.name}. Better luck next time!")
                exit()

            # Print player's current score
            print(f"\nCurrent score: {player.score}")

        # Print the final score after all questions have been answered
        print(f"Thanks for playing, {player.name}! Your final score is {player.score}")

game = Game()
game.play()
