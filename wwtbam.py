# Who wants to be a millionaire terminal game
# Class to store player information such as name and score
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    # Method to update player's score
    def update_score(self, score):
        self.score = score

# Class to store question information such as question number, question, options, and answer
class Question:
    def __init__(self, number, question, options, answer):
        self.number = number
        self.question = question
        self.options = options
        self.answer = answer

# Define the question_value list to hold the value of each question
question_value = [500, 1000, 2000, 5000, 10000, 20000, 50000, 75000, 1500000, 200000, 500000, 1000000]

# Class to handle the game
class Game:
    def __init__(self):
        self.questions = [
            Question(1, "What is the capital of France?", ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], "A"),
            Question(2, "What is the currency of Japan?", ["A. Dollar", "B. Euro", "C. Yen", "D. Pound"], "C"),
            Question(3, "What is the largest ocean in the world?", ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], "D"),
            Question(4, "Who painted the Mona Lisa?", ["A. Michelangelo", "B. Leonardo da Vinci", "C. Raphael", "D.Donatello"], "B")
            ]

    # Welcome message for the game
    def welcome_message(self):
        print("""
WHO WANTS TO BE A...
  __  __ _____ _      _      _____ ____  _   _          _____  ______ ___  
 |  \/  |_   _| |    | |    |_   _/ __ \| \ | |   /\   |  __ \|  ____|__ \ 
 | \  / | | | | |    | |      | || |  | |  \| |  /  \  | |__) | |__     ) |
 | |\/| | | | | |    | |      | || |  | | . ` | / /\ \ |  _  /|  __|   / / 
 | |  | |_| |_| |____| |____ _| || |__| | |\  |/ ____ \| | \ \| |____ |_|  
 |_|  |_|_____|______|______|_____\____/|_| \_/_/    \_\_|  \_\______|(_)  

        """)
        print("""
Welcome to WWTBAM! You will be asked a series of multiple-choice questions that each have four 
possible answers (A,B,C,D). You must answer all of these questions correctly, one at a time, in 
order to win the million dollars. As soon as you answer a question incorrectly, the game is over.
""")

    # Main method to run game
    def play(self):
        self.welcome_message()
        # Get the player's name and instantiate the player object
        player_name = input("Please enter your name: ")
        player = Player(player_name)

        # Loop through questions list
        for question in self.questions:
            print()
            print(f"Question {question.number}:") #print the question number
            print(question.question) #print the question
            print(*question.options, sep="\n") #print the options

            # Check to ensure the player's input is 'A', 'B', 'C', or 'D'
            while True:
                answer = input("Your answer: ").upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter a valid answer (A, B, C, or D)")

            # If the answer is correct, update the player's score and print "Correct!"
            if answer == question.answer:
                print("\nCorrect!")
                player.update_score(question_value[question.number - 1])
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
