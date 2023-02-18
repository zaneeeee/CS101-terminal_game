# Who wants to be a millionaire terminal game
import random

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
QUESTIONS = [
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
    },
    {
        'question': 'Who is the current President of the United States?',
        'options': ['Barack Obama', 'Donald Trump', 'Joe Biden', 'George W. Bush'],
        'answer': 'Joe Biden'
    },
    {
        'question': 'What is the largest desert in the world?',
        'options': ['Antarctica', 'Sahara Desert', 'Arabian Desert', 'Gobi Desert'],
        'answer': 'Sahara Desert'
    },
    {
        'question': 'What is the longest river in the world?',
        'options': ['Nile River', 'Amazon River', 'Yangtze River', 'Yellow River'],
        'answer': 'Nile River'
    },
    {
        'question': 'Who is the author of the Harry Potter series?',
        'options': ['J.K. Rowling', 'Stephen King', 'John Green', 'Suzanne Collins'],
        'answer': 'J.K. Rowling'
    },
    {
        'question': 'Who painted the famous artwork "The Starry Night"?',
        'options': ['Vincent van Gogh', 'Pablo Picasso', 'Rembrandt', 'Claude Monet'],
        'answer': 'Vincent van Gogh'
    },
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['Au', 'Ag', 'Fe', 'Al'],
        'answer': 'Au'
    },
    {
        'question': 'Who was the first man to walk on the moon?',
        'options': ['Neil Armstrong', 'Buzz Aldrin', 'Yuri Gagarin', 'John Glenn'],
        'answer': 'Neil Armstrong'
    },
    {
        'question': 'Who discovered America?',
        'options': ['Christopher Columbus', 'Leif Erikson', 'Marco Polo', 'Vasco da Gama'],
        'answer': 'Christopher Columbus'
    }
]

# Class to store player information such as name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __repr__(self):
        return f"{self.name}, your score is {self.score}"

    # Method to update player's score
    def update_score(self, index):
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
                print("Thanks for playing, " + repr(player))
                self.game_over()

            # Print player's current score
            print(repr(player))

        # Print the final score after all questions have been answered
        print("Thanks for playing, " + repr(player))
        self.game_over()

game = Game()
game.play()
