"""
CSE 111
Lesson 10 ICE Challenge - Handle Exceptions
Author: [Your Name Here]

Description:
Practice handling exceptions for each exception type that could
potentially come up in the process_inputs() function below
"""

def main():
    # Example inputs that could cause different exceptions. Try each of
    # these and add the appropriate try/except block to handle that
    # specific type of exception

    sample_inputs = ["apple", "5", "0", "example"]
    # sample_inputs = ["10", "5", "0", "example"]
    # sample_inputs = ["10", 5, 0, "example"]
    # sample_inputs = ["10", 5, 1]
    # sample_inputs = ["10", 5, 2, "example"]

    process_inputs(sample_inputs)


def process_inputs(inputs):
    try:
        # Potential ValueError: Converting a string to an integer
        number = int(inputs[0])

        # Potential TypeError: Attempting an unsupported operation
        result = number + inputs[1]

        # Potential ZeroDivisionError: Dividing by zero
        division = number / inputs[2]

        # Potential IndexError: Accessing an out-of-range list index
        item = inputs[3]

        print(f"Processed values: {result}, {division}, {item}")

    except ValueError as e:
        print("Error, must be a valid integer")

    except IndexError as e:
        print("Error, the inputs list must have at least 4 items")

    except TypeError as e:
        print("Error, must be a number")

    except ZeroDivisionError as e:
        print("Error, cannot divide by 0")


if __name__ == "__main__":
    main()
