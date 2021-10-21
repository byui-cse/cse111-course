# teach_solution.py
# Copyright 2020, Brigham Young University - Idaho. All rights reserved.

NEGATIVE = -1
POSITIVE = 1


def main():
    print("This program is an implementaiton of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += ask_question("1. I feel that I am a person of worth, at least on an equal plane with others.", POSITIVE)
    score += ask_question("2. I feel that I have a number of good qualities.", POSITIVE)
    score += ask_question("3. All in all, I am inclined to feel that I am a failure.", NEGATIVE)
    score += ask_question("4. I am able to do things as well as most other people.", POSITIVE)
    score += ask_question("5. I feel I do not have much to be proud of.", NEGATIVE)
    score += ask_question("6. I take a positive attitude toward myself.", POSITIVE)
    score += ask_question("7. On the whole, I am satisfied with myself.", POSITIVE)
    score += ask_question("8. I wish I could have more respect for myself.", NEGATIVE)
    score += ask_question("9. I certainly feel useless at times.", NEGATIVE)
    score += ask_question("10. At times I think I am no good at all.", NEGATIVE)

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_question(statement, pos_or_neg):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3

    if pos_or_neg == NEGATIVE:
        score = 3 - score

    return score


# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
