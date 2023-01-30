#who wants to be a millionaire terminal game
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
