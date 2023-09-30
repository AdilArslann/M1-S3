from question import Question

class Profile:
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.probabilities = {}
        self.scores = []

    def add_question(self, question):
        self.questions.append(question)
        self.probabilities[question] = 1.0

    def update_question_probability(self, question):
        self.probabilities[question] *= 0.8

    def get_question_probability(self, question):
        return self.probabilities.get(question, 1.0)

    def save_profile(self, filename):
        data = {
            "name": self.name,
            "questions": [question.to_dict() for question in self.questions],
            "probabilities": self.probabilities,
            "scores": self.scores
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    @classmethod
    def load_profile(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        profile = cls(data["name"])
        for question_data in data["questions"]:
            question = Question.from_dict(question_data)
            profile.add_question(question)
        profile.probabilities = data["probabilities"]
        profile.scores = data["scores"]
        return profile