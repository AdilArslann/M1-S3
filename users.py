class User:
    def __init__(self, username):
        self.username = username
        self.statistics = {}

    def update_statistics(self, question_id, correct):
        if question_id not in self.statistics:
            self.statistics[question_id] = {"shown": 0, "correct": 0}
        self.statistics[question_id]["shown"] += 1
        if correct:
            self.statistics[question_id]["correct"] += 1
