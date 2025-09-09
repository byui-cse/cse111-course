"""
CSE 111
Lesson 07 ICE - Lists and Repetition (Compound Lists)
Author: [Your Name Here]

Description:
Build and process a compound list that tracks student names, their
homework average, and their exam score.  Reinforces:

• Creating compound lists
• Mutating a list that is passed into a function (list mutability)
• Looping with both “for element in list” and index-based loops
• Using len, sum, max, and the membership operator

Instructions:
Write a program that:

  1. Contains a main() function that does the following:
       • Repeatedly asks the user for a student's name.
         - A blank name quits data entry.
       • For each student, asks for:
           - Homework average (0-100)
           - Exam score      (0-100)
       • Appends an inner list [name, hw, exam] to a compound list
         named "gradebook".

       • After data entry, prints:
           - Number of students
           - Class homework average  (two decimals)
           - Class exam average      (two decimals)
           - Student with highest exam score (name & score)

       • Calls curve_exams(gradebook, 5) to add 5 points to every
         exam score (cap at 100).

       • Prints the new exam average and a neat table of:
         Name, HW, Curved-Exam, Final Grade (0.4*HW + 0.6*Exam).

  2. Contains a helper function:
       def curve_exams(records, curve):
           '''
           Mutate each inner list so exam += curve (but not above 100).
           records is the compound list (gradebook).
           '''

  3. Uses index constants for readability:
       NAME_INDEX = 0
       HW_INDEX   = 1
       EXAM_INDEX = 2

  4. Only main() should handle all user input and printing except for
     optional debug prints used while troubleshooting.

  6. Stretch ideas (optional):
       • Make curve amount user-input.
       • Allow removal of a student with list.remove() or list.pop().
       • Replace the two numeric fields with another inner list to
         create a three-level structure.

Sample output:
Student name (blank to quit): bob
  Homework average (0-100): 80
  Exam score (0-100): 100
Student name (blank to quit): bill
  Homework average (0-100): 50
  Exam score (0-100): 98
Student name (blank to quit): jane
  Homework average (0-100): 50
  Exam score (0-100): 50
Student name (blank to quit):

Students: 3
HW   avg: 60.00
Exam avg: 82.67
Top exam: bob (100.0)

After +5 curve, new exam avg: 85.00

Name               HW    Exam   Final
bob              80.0   100.0    92.0
bill             50.0   100.0    80.0
jane             50.0    55.0    53.0
"""

# Index constants
NAME_INDEX  = 0
HW_INDEX    = 1
EXAM_INDEX  = 2


def main():
    """Collect data, compute stats, curve exams, and display results."""
    # TODO: Create an empty list called gradebook to hold inner lists.
    gradebook = []   # [["bob", 93, 99], ["bill", 88, 91], ...]

    # Data-entry loop
    # TODO: Repeatedly prompt for student's name, hw score, exam score.
    #       Append each [name, hw, exam] list to gradebook until the
    #       user submits a blank name to quit.

    # Stats BEFORE curving
    # TODO: Compute and print:
    #     • Number of students
    #     • Homework average
    #     • Exam average
    #     • Top student (name & highest exam score)

    # Curve exams in-place
    # TODO: Call curve_exams(gradebook, 5)

    # Stats AFTER curving
    # TODO: Compute and print new exam average

    # Display formatted table
    # TODO: Loop through gradebook and print Name, HW, Curved Exam, Final


def curve_exams(records, curve):
    """
    Mutate each inner list so its exam score is increased by `curve`
    points without exceeding 100.

    Parameters
        records: compound list (list of [name, hw, exam])
        curve:   amount to add to each exam score
    """
    # TODO: Loop through each inner list and adjust the EXAM_INDEX element.


# Run the program
if __name__ == "__main__":
    main()
