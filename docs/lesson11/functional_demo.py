"""
Use all or any part of this file as a demonstration of functional
programming during class in your section of CSE 111.

You could retain the numbered comments and delete all or any parts of
the code. Then give the modified file to your students and ask them to
write the code for the numbered comments. Or you could write the code
for the numbered comments with them as a demonstration during class.

Copyright 2024, Brigham Young University - Idaho. All rights reserved.
"""

def main():
    students = [
        # First Name,Last Name,Gender,Birth Date,City,State
        ["Brian", "Morales", "Male", "1998-08-30", "Gretna", "Virginia"],
        ["Jennifer", "Burns", "Female", "2001-08-09", "Ririe", "Idaho"],
        ["Sharon", "Williams", "Female", "2000-01-16", "Macon", "Georgia"],
        ["Sean", "Taylor", "Male", "2001-08-02", "Ocala", "Florida"],
        ["Christopher", "Burns", "Male", "2001-12-26", "Bend", "Oregon"],
        ["Terri", "Rogers", "Female", "2004-10-24", "Tifton", "Georgia"],
        ["Sherri", "Morales", "Female", "1998-11-30", "Albany", "Georgia"],
        ["Angela", "Morales", "Female", "2005-09-12", "Athens", "Georgia"],
        ["Robert", "Adams", "Male", "2004-04-22", "Clover", "Virginia"],
        ["Jose", "Weeks", "Male", "2002-03-29", "Sebring", "Florida"]
    ]

    print("\nNot Sorted")
    print_list(students)

    # 1. Call the built-in sorted function to sort the
    # students list by the students' last name.
    by_last_name = sorted(students, key=extract_last_name)
    print("\nSorted by Last Name")
    print_list(by_last_name)

    # 2. Call the built-in sorted function to sort the
    # students list by both last and first names.
    by_name = sorted(students, key=extract_last_and_first_name)
    print("\nSorted by Last Name and First Name")
    print_list(by_name)

    # 3. Write a small nested function named extract_birthdate
    # and use that function in a call to the built-in sorted
    # function to sort the students list by birthdate.
    def extract_birthdate(one_student):
        return one_student[3]

    by_birthdate = sorted(students, key=extract_birthdate)
    print("\nSorted by Birthdate")
    print_list(by_birthdate)

    # 4. Call the built-in sorted function and pass a lambda function
    # as the key in order to sort the students list by state name.
    by_state = sorted(students, key=lambda one_student: one_student[5])
    print("\nSorted by State Name")
    print_list(by_state)


LAST_NAME_INDEX = 1
def extract_last_name(one_student):
    return one_student[LAST_NAME_INDEX]

def extract_last_and_first_name(one_student):
    first_name = one_student[0]
    last_name = one_student[1]
    return f"{last_name} {first_name}"

def print_list(students):
    for student in students:
        print(student)


if __name__ == "__main__":
    main()
