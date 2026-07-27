"""
CSE 111
Practice writing Python code that uses a dictionary.
"""
import csv


def main():
    # 1. Create an empty dictionary.
    tools_dict = {}

    # 2. Put one cooking tool into the empty dictionary.
    tools_dict["p135"] = "whisk"

    # 3. Put another cooking tool into the tools dictionary.
    tools_dict["p310"] = "slotted spoon"

    # 4. Prompt the user to enter three more cooking
    # tools and put those in the tools dictionary.
    print("Please enter the tool number and name for three cooking tools.")
    for _ in range(3):
        key = input("Enter a cooking tool's number: ")
        value = input("Enter the cooking tool's name: ")
        tools_dict[key] = value

    # 5. Print the entire cooking tools dictionary.
    print(tools_dict)
    print()

    # 6. Prompt the user to enter a tool key. Find
    # and then print the corresponding tool name.
    key = input("Enter a tool's number: ")

    if key in tools_dict:
        # Here it is! This is how to find something in a
        # dictionary. Many students miss this point. This is how
        # to do it. It's simple. value = dictionary_name[key]
        value = tools_dict[key]
        print(value)
    else:
        print(f"Tool number {key} doesn't exist")
    print()


    # 7. Create another dictionary with four key value pairs.
    clothing_dict = {
        "c75" : "Jacket",
        "c42" : "Shirt",
        "c10" : "Socks",
        "c14" : "Socks"
    }

    # 8. Print the entire clothing dictionary.
    print(clothing_dict)
    print()

    # 9. Print just the keys from the clothing dictionary.
    print(clothing_dict.keys())
    print()

    # 10. Print just the values from the clothing dictionary.
    print(clothing_dict.values())
    print()

    # 11. Print the key value pairs as items from the clothing dictionary.
    print(clothing_dict.items())
    print()

    # 12. Print the items in the clothing dictionary, one at a time.
    for key, value in clothing_dict.items():
        print(key, value)
    print()

    # Although printing a dictionary is interesting, the real
    # reason to create a dictionary is to use the keys to find
    # values. Dictionaries are very fast at finding items.


    # 13. Use the csv module to write the clothing dictionary to a CSV file.
    print("Writing the clothing dictionary to a csv file.")
    with open("clothing.csv", "wt", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write column headings to the CSV file.
        writer.writerow(["Clothing Number", "Clothing Number"])

        for item in clothing_dict.items():
            writer.writerow(item)

    print("To see the clothing.csv file, open it in VS Code.")
    print()

    # 14. Use the csv module to read the
    # clothing.csv file into a new dictionary.
    print("Reading the csv file into a new dictionary.")
    things_dict = {}
    with open("clothing.csv", "rt") as csvfile:
        reader = csv.reader(csvfile)

        # Skip the first line of the clothing.csv file because
        # the first line contains column headings, and we don't
        # want to add the column headings to the dictionary.
        next(reader)

        for row_list in reader:
            clothing_number = row_list[0]
            clothing_name = row_list[1]
            things_dict[clothing_number] = clothing_name

    print(things_dict)
    print()


if __name__ == "__main__":
    main()
