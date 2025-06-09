class Student:
    def __init__(self, name):
        self.student_name = name
        self.questions = []
        
    def add_question(self,question):
        self.questions.append(question)
        
    def get_number_of_questions(self):
        return len(self.questions)
        
    def calculate_score(self, answers):
        total = 0
        for x in range(len(answers)):
            if self.questions[x].is_correct(answers[x]):
                total += 1
                
        return total