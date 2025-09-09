"""
CSE 111
Lesson 10 ICE - Handling Exceptions
Author: [Your Name]

Description:
Practice building a compound dictionary from user input where the keys
are employee IDs and the values are a list of [name, sandwiches_made].

Use try / except to handle:
    ValueError  (bad integer input)
    KeyError    (duplicate employee ID)
    ZeroDivisionError (no employees when computing average)
    KeyboardInterrupt (prevent Ctrl+C)

Program Requirements
1. Repeatedly prompt the user to enter data for one employee in the form:
       ID  Name  Sandwiches
   Example:
       101  Alice  30

   • Use a single input line or three separate prompts—your choice.
   • Use the word "done" to stop entry.

2. Validate and store each entry in a dictionary named employees
   where:
       key is employee ID (string or int)
       value is [name (str), sandwiches_made (int)]

   • If the user enters a non-integer for sandwiches, handle the
     ValueError, warn, and reprompt.
   • If the user re-uses an existing ID, handle the KeyError
     (or check membership), warn, and reprompt.

3. After data entry ends, compute and display:
   • Total sandwiches made
   • Average sandwiches per employee (handle ZeroDivisionError)

4. Use index constants for the inner list:
   NAME_INDEX  = 0
   COUNT_INDEX = 1

Stretch Goals
  • Allow the user to update an existing employee's sandwich count.
  • Write the final dictionary to a CSV file and handle PermissionError.
"""

# index constants
NAME_INDEX  = 0
COUNT_INDEX = 1


def main():
    employees = {}

    print("Enter employee data (ID Name Sandwiches). Type 'done' to finish.")

    while True:
        # TODO: Your code here
        entry = input("> ")
        if entry.lower() == "done":
            break

        id, name, count = entry
        print(id, name, count)

    # Results
    try:
        # TODO your code here to compute total sandwiches made
        #      and the average per employee
        ...
    except ZeroDivisionError:
        print("\nNo employee data entered.")


if __name__ == "__main__":
    main()
