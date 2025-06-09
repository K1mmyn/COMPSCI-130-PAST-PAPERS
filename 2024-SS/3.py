class Question:
    def __init__(self, question_id, question_stem, correct_answer):
        self.question_id = question_id
        self.question_stem = question_stem
        self.correct_answer = correct_answer.lower()
        
    def __str__(self):
        return f"({self.question_id}) {self.question_stem}[{self.correct_answer}]"
        
    def is_correct(self, answer):
        return self.correct_answer == answer.lower()