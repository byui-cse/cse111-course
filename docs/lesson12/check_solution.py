# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def main():
    try:
        # Create and print a list named fruit_list.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        # Reverse and print the fruit_list list.
        fruit_list.reverse()
        print(f"reversed: {fruit_list}")

        # Append "orange" to the end of the fruit_list and
        # print the list.
        fruit_list.append("orange")
        print(f"append orange: {fruit_list}")

        # Find where "apple" is located in the fruit_list and insert
        # "cherry" before "apple" in the list and print the list.
        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")

        # Remove "banana" from the fruit_list and print the list.
        fruit_list.remove("banana")
        print(f"remove banana: {fruit_list}")

        # Pop (remove) the last element from the fruit_list
        # and print the popped element and the list.
        last = fruit_list.pop()
        print(f"pop {last}: {fruit_list}")

        # Sort and print the fruit_list.
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        # Clear and print the fruit_list.
        fruit_list.clear()
        print(f"cleared: {fruit_list}")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


# If this file is executed like this:
# > python check_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
