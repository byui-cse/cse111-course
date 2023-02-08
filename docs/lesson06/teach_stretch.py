# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

NEGATIVE = -1
POSITIVE = 1


def main():
    print("This program is an implementation of the Nature")
    print("Relatedness Scale developed by Nisbet, Zelenski,")
    print("and Murphy. This program will show you 21 statements")
    print("that you could possibly apply to yourself. Please")
    print("rate how much you agree with each of the statements")
    print("by responding with one of these five letters:")
    print()
    print("D means you disagree strongly with the statement.")
    print("d means you disagree a little with the statement.")
    print("n means you neither agree nor disagree with the statement.")
    print("a means you agree a little with the statement.")
    print("A means you agree strongly with the statement.")
    print()

    score = 0
    score += ask_question("1. My connection to nature and the"
        " environment is a part of my spirituality.", POSITIVE)
    score += ask_question("2. My relationship to nature is an"
        " important part of who I am.", POSITIVE)
    score += ask_question("3. I feel very connected to all living"
        " things and the earth.", POSITIVE)
    score += ask_question("4. I am not separate from nature, but a part"
        " of nature.", POSITIVE)
    score += ask_question("5. I always think about how my actions"
        " affect the environment.", POSITIVE)
    score += ask_question("6. I am very aware of environmental issues.",
        POSITIVE)
    score += ask_question("7. I think a lot about the suffering of"
        " animals.", POSITIVE)
    score += ask_question("8. Even in the middle of the city, I notice"
        " nature around me.", POSITIVE)
    score += ask_question("9. My feelings about nature do not affect"
        " how I live my life.", NEGATIVE)
    score += ask_question("10. Humans have the right to use natural"
        " resources any way we want.", NEGATIVE)
    score += ask_question("11. Conservation is unnecessary because"
        " nature is\n    strong enough to recover from any human impact.",
        NEGATIVE)
    score += ask_question("12. Animals, birds and plants have fewer"
        " rights than humans.", NEGATIVE)
    score += ask_question("13. Some species are just meant to die out"
        "or become extinct.", NEGATIVE)
    score += ask_question("14. Nothing I do will change problems in"
        " other places on the planet.", NEGATIVE)
    score += ask_question("15. The state of nonhuman species is an"
        " indicator of the future for humans.", POSITIVE)
    score += ask_question("16. The thought of being deep in the woods,"
        " away\n    from civilization, is frightening.", NEGATIVE)
    score += ask_question("17. My ideal vacation spot would be a"
        " remote, wilderness area.", POSITIVE)
    score += ask_question("18. I enjoy being outdoors, even in"
        " unpleasant weather.", POSITIVE)
    score += ask_question("19. I don’t often go out in nature.",
        NEGATIVE)
    score += ask_question("20. I enjoy digging in the earth and getting"
        " dirt on my hands.", POSITIVE)
    score += ask_question("21. I take notice of wildlife wherever I am.",
        POSITIVE)

    print()
    print(f"Your score is {score}.")
    print("The lowest possible score is 21.")
    print("The highest possible score is 105.")


def ask_question(statement, pos_or_neg):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("  Enter D, d, n, a, or A: ")
    score = 0
    if answer == 'D':
        score = 1
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 4
    elif answer == 'A':
        score = 5
    else:  # answer == 'n'
        score = 3

    if pos_or_neg == NEGATIVE:
        # This is a negative question, and the scores for
        # negative questions are the opposite of scores for
        # positive questions. Therefore, to calculate a score
        # for a negative question, we subtract the postive
        # score from the maximum score plus 1 (5 + 1 = 6).
        score = 6 - score

    return score


# If this file was executed like this:
# > python nature.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
