import json

class Question:
    def __init__(self, question_text, answer_options=None, correct_answer=None):
        self.question_text = question_text
        self.answer_options = answer_options
        self.correct_answer = correct_answer
        self.active = True
        self.show_count = 0
        self.correct_count = 0

    def is_correct(self, user_answer):
        if self.correct_answer is not None:
            return user_answer.lower() == self.correct_answer.lower()
        return False

    def get_correctness_percentage(self):
        if self.show_count == 0:
            return 0
        return (self.correct_count / self.show_count) * 100

    def toggle_active(self):
        self.active = not self.active

    def increment_show_count(self):
        self.show_count += 1

    def increment_correct_count(self):
        self.correct_count += 1

    def to_dict(self):
        return {
            "question_text": self.question_text,
            "answer_options": self.answer_options,
            "correct_answer": self.correct_answer,
            "active": self.active,
            "show_count": self.show_count,
            "correct_count": self.correct_count
        }

    @classmethod
    def from_dict(cls, data):
        question = cls(
            data["question_text"],
            data["answer_options"],
            data["correct_answer"]
        )
        question.active = data["active"]
        question.show_count = data["show_count"]
        question.correct_count = data["correct_count"]
        return question

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            return cls.from_dict(data)

    def get_average_correctness_percentage(self):
        if self.show_count == 0:
            return 0
        return (self.correct_count / self.show_count) * 100
