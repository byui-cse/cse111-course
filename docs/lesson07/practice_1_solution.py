"""
CSE 111
Lesson 7 - Repetition (Loops) and Lists

Practice writing loops by completing each of the exercises below.
"""

def main():
    # In the code below, there are seven tasks. Each task is described
    # in a comment. Then each task is implemented one or more times. The
    # last implementation is the preferred way in Python of implementing
    # the task.

    # 1. Write a loop that prints the integers
    # between zero and ten, including zero and ten.
    i = 0
    while i < 11:
        print(i)
        i += 1

    for i in range(11):
        print(i)

    # Print a blank line.
    print()

    # 2. Write a loop that prints the integers
    # between three and ten, including three and ten.
    i = 3
    while i < 11:
        print(i)
        i += 1

    for i in range(3, 11):
        print(i)

    # Print a blank line.
    print()

    # 3. Write a loop that prints the integers 20, 25, 30, 35.
    i = 20
    while i < 40:
        print(i)
        i += 5

    for i in range(20, 40, 5):
        print(i)

    # Print a blank line.
    print()

    # 4. Write a loop that prints the integers 40, 38, 36, 34, 32, 30.
    i = 40
    while i > 28:
        print(i)
        i -= 2

    for i in range(40, 28, -2):
        print(i)

    # Print a blank line.
    print()

    # 5. Write a loop that stores the integers from
    # zero to ten in a list. Include zero and ten.
    integers = []
    i = 0
    while i < 11:
        integers.append(i)
        i += 1
    print(integers)

    integers = []
    for i in range(11):
        integers.append(i)
    print(integers)

    # Print a blank line.
    print()

    # 6. Write a loop that prints each element in a list on a different line.
    people = ["James", "Lisa", "Juan", "Sophia", "William", "Noah", "Olivia"]

    i = 0
    while i < len(people):
        person = people[i]
        print(person)
        i += 1

    for i in range(len(people)):
        person = people[i]
        print(person)

    for person in people:
        print(person)

    # Print a blank line.
    print()

    # 7. Below are two parallel lists. Write a loop that prints the elements
    # of both lists to a terminal window on separate lines like this:
    # Ashton 97
    # Chester 75
    # Drummond 83
    # Felt 72
    # Island Park 154
    # Wayan 78
    cities = ["Ashton", "Chester", "Drummond", "Felt", "Island Park", "Wayan"]
    snowfall = [97, 75, 83, 72, 154, 78]  # inches

    i = 0
    while i < len(cities):
        city = cities[i]
        inches = snowfall[i]
        print(f"{city} {inches}")
        i += 1

    for i in range(len(cities)):
        city = cities[i]
        inches = snowfall[i]
        print(f"{city} {inches}")

    for city, inches in zip(cities, snowfall):
        print(f"{city} {inches}")

    # Print a blank line.
    print()


if __name__ == "__main__":
    main()
