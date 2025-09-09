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
        try:
            entry = input("> ")
            if entry.lower() == "done":
                break

            emp_id, name, sand_count = entry.split()

            # Check duplicate ID
            if emp_id in employees:
                # Option 1 is to raise a key error which will
                # be handled in the except KeyError block below.
                raise KeyError(f"ID {emp_id} already exists.")

                # Option 2 is to ignore the input and print a message
                # print(f"ID {emp_id} already exists.")
                # continue

            # Convert sandwiches to int
            sandwiches = int(sand_count)

            employees[emp_id] = [name, sandwiches]

        except ValueError as e:
            print("  Error: please enter as  ID Name SandwichesMade (Sandwiches must be an integer).")
        except KeyError as e:
            print("  Error:", e)
        except KeyboardInterrupt:
            print("Don't do that!")
        except Exception as e:
            print(e)

    # Results
    try:
        # Option 1 using for loop
        total = 0
        for name, count in employees.values():
            total += count

        # Option 2 using list comprehension
        total = sum(info[COUNT_INDEX] for info in employees.values())

        avg   = total / len(employees)

        print(f"\nTotal sandwiches: {total}")
        print(f"Average per employee: {avg:.1f}")

    except ZeroDivisionError:
        print("\nNo employee data entered.")


if __name__ == "__main__":
    main()
