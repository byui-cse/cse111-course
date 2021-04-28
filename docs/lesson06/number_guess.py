import random


def main():
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print()

    prompt = "Please enter an integer between 1 and 100: "
    answer = random.randint(1, 100)
    guess = -1
    tries = 0

    while guess != answer:
        # Get a guess from the user.
        guess = int(input(prompt))
        tries += 1

        # Compare the user's guess to the answer.
        if guess < answer:
            prompt = f"{guess} is too low. Please enter another integer: "
        elif guess < answer:
            prompt = f"{guess} is too high. Please enter another integer: "

    print()
    print(f"{guess} is correct!")
    print(f"You used {tries} guesses to guess my number.")


# If this file was executed like this:
# > python number_guess.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
