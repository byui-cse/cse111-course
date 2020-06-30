def main():
    # Create and print a list named fruit.
    fruit = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit}")

    # Reverse and print the fruit list.
    fruit.reverse()
    print(f"reversed: {fruit}")

    # Append "orange" to the end of the fruit list and print the list.
    fruit.append("orange")
    print(f"append orange: {fruit}")

    # Find where "apple" is located in the fruit list and insert
    # "cherry" before "apple" in the list and print the list.
    pos = fruit.index("apple")
    fruit.insert(pos, "cherry")
    print(f"insert cherry: {fruit}")

    # Remove "banana" from the fruit list and print the list.
    fruit.remove("banana")
    print(f"remove banana: {fruit}")

    # Pop (remove) the last element from the fruit
    # list and print the popped element and the list.
    last = fruit.pop()
    print(f"pop: {last} {fruit}")

    # Sort and print the fruit list.
    fruit.sort()
    print(f"sorted: {fruit}")

    # Clear and print the fruit list.
    fruit.clear()
    print(f"cleared: {fruit}")


main()
