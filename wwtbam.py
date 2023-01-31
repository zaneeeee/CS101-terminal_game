#who wants to be a millionaire terminal game
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def update_score(self, score):
        self.score = score

class Question:
    def __init__(self, number, question, options, answer):
        self.number = number
        self.question = question
        self.options = options
        self.answer = answer

class Game:
    def __init__(self):
        self.questions = [
            Question(1, "What is the capital of France?", ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], "A"),
            Question(2, "What is the currency of Japan?", ["A. Dollar", "B. Euro", "C. Yen", "D. Pound"], "C"),
            Question(3, "What is the largest ocean in the world?", ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], "D"),
            Question(4, "Who painted the Mona Lisa?", ["A. Michelangelo", "B. Leonardo da Vinci", "C. Raphael", "D.Donatello"], "B")
]

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
        print("""Welcome to WWTBAM! You will be asked a series of multiple-choice questions that each have four 
possible answers (A,B,C,D). You must answer all of these questions correctly, one at a time, in 
order to win the million dollars. As soon as you answer a question incorrectly, the game is over.
""")

    def play(self):
        self.welcome_message()
        player_name = input("Please enter your name: ")
        player = Player(player_name)
        
        for q in self.questions:
            print()
            print("Question {}:".format(q.number))
            print(q.question)
            print(*q.options, sep="\n")
            
            #Add check to ensure the user's input is 'A', 'B', 'C', or 'D'
            while True:
                answer = input("Your answer: ").upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter a valid answer (A, B, C, or D)")

            if answer == q.answer:
                print("\nCorrect!")
                player.update_score(question_value[q.number - 1])
            else:
                print("\nIncorrect!")
                print("\n GAME OVER")
                exit()
            
            print("\nCurrent score: ${}".format(player.score))

        print("Thanks for playing, {name}! Your final score is ${score}".format(name=player.name, score=player.score))

question_value = [500,1000,2000,5000,10000,20000,50000,75000,1500000,200000, 500000, 1000000]

game = Game()
game.play()
