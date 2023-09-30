# Interactive Learning Tool

Welcome to the Interactive Learning Tool! This program allows you to create, practice, and test your knowledge using multiple-choice and freeform text questions. It also tracks your statistics and provides options to manage your questions. This README will guide you through using the program and provide some technical insights for those interested.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Modes](#modes)
   - [Adding Questions Mode](#adding-questions-mode)
   - [Statistics Viewing Mode](#statistics-viewing-mode)
   - [Disable/Enable Questions Mode](#disableenable-questions-mode)
   - [Practice Mode](#practice-mode)
   - [Test Mode](#test-mode)
   - [Bonus: Profile Select](#bonus-profile-select)
3. [Technical Details](#technical-details)
---

## Getting Started <a name="getting-started"></a>

Before you begin, make sure you have Python installed on your computer. You can download it from [Python's official website](https://www.python.org/downloads/).

To use this program:

1. Clone this GitHub repository: [link-to-your-repo](https://github.com/AdilArslann/M1-S3)
2. Open your terminal and navigate to the project directory.
3. Run the program by executing `python main.py`.

Now, let's explore the available modes and functionalities.

## Modes <a name="modes"></a>

### Adding Questions Mode <a name="adding-questions-mode"></a>

In this mode, you can add two types of questions:

1. Quiz Questions: Multiple-choice questions where you provide options and specify the correct answer.
2. Free-Form Text Questions: Open-ended questions where you specify the expected answer as text.

Questions are saved in a file, so they persist even after you close the program. You must add at least 5 questions before accessing other modes.

### Statistics Viewing Mode <a name="statistics-viewing-mode"></a>

This mode displays a list of all questions. Each question is associated with:

- A unique ID
- Active or not
- Question text
- Times shown during practice/tests
- Percentage of correct answers

### Disable/Enable Questions Mode <a name="disableenable-questions-mode"></a>

You can disable or enable questions by entering their unique IDs. The question's details will be displayed for confirmation. Disabled questions won't appear in practice and test modes.

### Practice Mode <a name="practice-mode"></a>

Practice mode presents questions continuously. The program adjusts question probabilities, making incorrectly answered questions more likely to appear. This helps you focus on your weak areas.

### Test Mode <a name="test-mode"></a>

In Test mode, you select the number of questions for a test. Questions are chosen randomly, and each question appears at most once. After completing the test, you'll see your score, which is saved with a timestamp in a `results.txt` file.

### Bonus: Profile Select <a name="bonus-profile-select"></a>

This optional feature allows you to create profiles with individual statistics and question probabilities for practice mode. Test scores also display the profile that achieved them. Questions are shared among all profiles.

## Technical Details <a name="technical-details"></a>

- Object-Oriented Programming (OOP) is used for code organization.
- Regular expressions are employed in at least one function.
- File input/output is used to store questions and test results.
- Unit tests are included to ensure code reliability.