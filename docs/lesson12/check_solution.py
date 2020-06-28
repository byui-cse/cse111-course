def main():
    fruit = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit}")

    fruit.reverse()
    print(f"reversed: {fruit}")

    fruit.append("orange")
    print(f"append orange: {fruit}")

    pos = fruit.index("apple")
    fruit.insert(pos, "cherry")
    print(f"insert cherry: {fruit}")

    fruit.remove("banana")
    print(f"remove banana: {fruit}")

    fruit.sort()
    print(f"sorted: {fruit}")

    fruit.clear()
    print(f"cleared: {fruit}")


main()
