import os
import json
import random
from datetime import datetime
from question import Question
#from profile import Profile

QUESTION_FILE = os.path.join(os.path.dirname(__file__), "questions.json")
PROFILE_FILE = os.path.join(os.path.dirname(__file__), "profiles.json")

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
    
    @classmethod
    def from_dict(cls, data):
        profile = cls(data["name"])
        for question_data in data["questions"]:
            question = Question.from_dict(question_data)
            profile.add_question(question)
        profile.probabilities = data["probabilities"]
        profile.scores = data["scores"]
        return profile


    def to_dict(self):
        return {
            "name": self.name,
            "questions": [question.to_dict() for question in self.questions],
            "probabilities": self.probabilities,
            "scores": self.scores
        }

class Application:
    def __init__(self):
        self.questions = []
        self.active_profile = None
        self.profiles = {}

    def start(self):
        self.load_questions()  # Load questions from file
        self.load_profiles()  # Load profiles from file
        self.show_menu()


    def load_questions(self):
        if os.path.isfile(QUESTION_FILE):
            with open(QUESTION_FILE, "r") as file:
                question_data = json.load(file)
                self.questions = [Question.from_dict(data) for data in question_data]

    def load_profiles(self):
        if os.path.isfile(PROFILE_FILE):
            with open(PROFILE_FILE, "r") as file:
                profile_data = json.load(file)
                self.profiles = {data["name"]: Profile.from_dict(data) for data in profile_data}


    def save_questions(self):
        question_data = [question.to_dict() for question in self.questions]
        with open(QUESTION_FILE, "w") as file:
            json.dump(question_data, file)

    def save_profiles(self):
        profile_data = [profile.to_dict() for profile in self.profiles.values()]
        with open(PROFILE_FILE, "w") as file:
            json.dump(profile_data, file)

    
    def show_menu(self):
        print("Welcome to the Interactive Learning Tool!")
        while True:
            print("\nMain Menu:")
            print("1. Create Profile")
            print("2. Select Profile")
            print("3. Adding Questions")
            print("4. Statistics Viewing")
            print("5. Disable/Enable Questions")
            print("6. Practice Mode")
            print("7. Test Mode")
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_profile()
            elif choice == "2":
                self.select_profile()
            elif choice == "3":
                self.add_questions()
            elif choice == "4":
                self.view_statistics()
            elif choice == "5":
                self.toggle_question_status()
            elif choice == "6":
                self.practice_mode()
            elif choice == "7":
                self.test_mode()
            elif choice == "0":
                self.save_questions()  # Save questions to file
                self.save_profiles()  # Save profiles to file
                break
            else:
                print("Invalid choice. Please try again.")

    def add_questions(self):
        print("\nAdding Questions")
        while True:
            print("\nQuestion Types:")
            print("1. Quiz Question")
            print("2. Free-form Text Question")
            print("0. Back to Main Menu")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_quiz_question()
            elif choice == "2":
                self.add_freeform_question()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_quiz_question(self):
        print("\nAdding Quiz Question")
        question_text = input("Enter the question text: ")
        if not question_text:
            print("Question text cannot be empty")
            return

        answer_options = input("Enter the answer options (comma-separated): ").split(",")
        if not answer_options:
            print("Answer options cannot be empty")
            return

        correct_answer = input("Enter the correct answer: ")
        question = Question(question_text, answer_options, correct_answer)
        self.questions.append(question)
        print("Quiz question added successfully!")


    def add_freeform_question(self):
        print("\nAdding Free-form Text Question")
        question_text = input("Enter the question text: ")
        expected_answer = input("Enter the expected answer: ")
        question = Question(question_text, correct_answer=expected_answer)
        self.questions.append(question)
        print("Free-form text question added successfully!")

    def view_statistics(self):
        print("\nStatistics Viewing")
        if not self.questions:
            print("No questions found.")
        else:
            for question in self.questions:
                print(f"Question ID: {self.questions.index(question) + 1}")
                print(f"Active: {question.active}")
                print(f"Question: {question.question_text}")
                print(f"Shown Count: {question.show_count}")
                print(f"Correctness Percentage: {question.get_correctness_percentage()}%")
                print(f"Average Correctness Percentage: {question.get_average_correctness_percentage()}%\n")



    def toggle_question_status(self):
        print("\nDisable/Enable Questions")
        if not self.questions:
            print("No questions found.")
        else:
            question_id = int(input("Enter the ID of the question to disable/enable: ")) - 1
            if 0 <= question_id < len(self.questions):
                question = self.questions[question_id]
                print("Question Details:")
                print(f"Question: {question.question_text}")
                print(f"Answer Options: {question.answer_options}")
                print(f"Correct Answer: {question.correct_answer}")
                print(f"Active: {question.active}")

                choice = input("Do you want to disable/enable this question? (y/n): ")
                if choice.lower() == "y":
                    question.toggle_active()
                    print("Question status updated successfully!")
                else:
                    print("Question status not changed.")
            else:
                print("Invalid question ID.")



    #Practice mode
    def practice_mode(self):
        print("\nPractice Mode")
        if len(self.questions) < 5:
            print("At least 5 questions are required to enter Practice Mode.")
            return

        while True:
            question = self.select_question_for_practice()
            if not question:
                print("All questions have been answered correctly. Practice Mode ends.")
                break

            print(f"\nQuestion: {question.question_text}")

            if question.is_quiz_question():
                self.present_quiz_question(question)
            else:
                self.present_freeform_question(question)

            self.update_question_statistics(question, user_answer)

    def select_question_for_practice(self):
        active_questions = [question for question in self.questions if question.active]
        correct_count_sum = sum(question.correct_count for question in active_questions)

        if correct_count_sum == 0:
            return random.choice(active_questions)

        question_probabilities = [
            self.active_profile.get_question_probability(question)
            for question in active_questions
        ]
        question = random.choices(active_questions, weights=question_probabilities)[0]

        return question

    def present_quiz_question(self, question):
        print("Answer Options:")
        for i, option in enumerate(question.answer_options):
            print(f"{i + 1}. {option}")

        user_choice = input("Enter your choice: ")
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(question.answer_options):
            selected_option = question.answer_options[int(user_choice) - 1]
            if question.is_correct(selected_option):
                print("Correct!")
            else:
                print("Incorrect.")
        else:
            print("Invalid choice. Please try again.")

    def present_freeform_question(self, question):
        user_answer = input("Enter your answer: ")
        if question.is_correct(user_answer):
            print("Correct!")
        else:
            print("Incorrect.")

    def update_question_statistics(self, question, user_answer):
        question.show_count += 1
        if question.is_correct(user_answer):
            question.correct_count += 1





    ##test Mode

    def test_mode(self):
        print("\nTest Mode")
        if len(self.questions) < 5:
            print("At least 5 questions are required to enter Test Mode.")
            return

        num_questions = self.select_num_test_questions()
        if num_questions == 0:
            return

        test_questions = random.sample(self.questions, min(num_questions, len(self.questions)))
        score = self.present_test_questions(test_questions)

        self.save_test_score(score)

    def select_num_test_questions(self):
        num_questions = int(input("Enter the number of questions for the test: "))
        if num_questions < 1 or num_questions > len(self.questions):
            print("Invalid number of questions. Please try again.")
            return 0
        return num_questions

    def present_test_questions(self, test_questions):
        score = 0
        for i, question in enumerate(test_questions):
            print(f"\nQuestion {i + 1}: {question.question_text}")
            if question.is_quiz_question():
                self.present_quiz_question(question)
            else:
                self.present_freeform_question(question)

            if question.correct:
                self.active_profile.update_question_probability(question)

        print("\nTest completed!")
        print(f"Score: {score}/{len(test_questions)}")
        return score

    def save_test_score(self, score):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score_data = {"timestamp": timestamp, "score": score}
        with open("results.txt", "a") as file:
            file.write(json.dumps(score_data) + "\n")




    #PROFILES

    def profile_select(self):
        print("\nProfile Select")
        if not self.profiles:
            print("No profiles found. Create a new profile.")
            self.create_profile()
        else:
            while True:
                print("Available Profiles:")
                for profile_name in self.profiles.keys():
                    print(f"- {profile_name}")

                choice = input("Enter the name of the profile to select (0 to create a new profile): ")
                if choice == "0":
                    self.create_profile()
                    break
                elif choice in self.profiles:
                    self.active_profile = self.profiles[choice]
                    print(f"Profile '{choice}' has been selected.")
                    break
                else:
                    print("Invalid profile name. Please try again.")


    def create_profile(self):
        print("\nCreate Profile")
        name = input("Enter your name: ")
        profile = Profile(name)
        self.profiles[name] = profile
        print(f"Profile '{name}' created successfully.")


    def select_profile(self):
        print("\nSelect Profile")
        name = input("Enter your name: ")
        if name in self.profiles:
            self.active_profile = self.profiles[name]
            print(f"Profile '{name}' selected.")
        else:
            print(f"Profile '{name}' not found.")


    def save_profile(self):
        if self.active_profile is not None:
            filename = f"{self.active_profile.name}.json"
            self.active_profile.save_profile(filename)
            print(f"Profile saved as {filename}")

    def load_profile(self):
        profile_name = input("Enter the name of the profile to load: ")
        filename = f"{profile_name}.json"
        try:
            profile = Profile.load_profile(filename)
            self.active_profile = profile
            print(f"Profile {profile_name} loaded successfully")
        except FileNotFoundError:
            print(f"Profile {profile_name} not found")



def main():
    app = Application()
    app.start()

if __name__ == "__main__":
    main()