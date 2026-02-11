"""
CSE 111
Lesson 7 - Repetition and Lists (Compound Lists)
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
    # Create an empty list called gradebook to hold inner lists.
    gradebook = []   # [["bob", 93, 99], ["bill", 88, 91], ...]

    # Data-entry loop
    # Repeatedly prompt for student's name, hw score, exam score.
    # Append each [name, hw, exam] list to gradebook until the
    # user submits a blank name to quit.

    while True:
        name = input("Student name (blank to quit): ")
        if name == "":
            break
        homework_average = float(input("Homework average: "))
        exam_average = float(input("Exam average: "))
        gradebook.append([name, homework_average, exam_average])

    # Stats BEFORE curving
    # Compute and print:
    #     • Number of students
    #     • Homework average
    #     • Exam average
    #     • Top student (name & highest exam score)

    # Number of students
    print(f"\nStudents: {len(gradebook)}")

    # Compute exam average
    hw_average, exam_average, top_name, top_score = compute_averages(gradebook)

    print(f"HW   avg: {hw_average:.2f}")
    print(f"Exam avg: {exam_average:.2f}")
    print(f"Top exam: {top_name} ({top_score})")

    # Curve exams in-place
    curve_amount = 5
    curve_exams(gradebook, curve_amount)

    # Stats AFTER curving
    # Compute and print new exam average
    hw_average, exam_average, top_name, top_score = compute_averages(gradebook)

    print(f"\nAfter +{curve_amount} curve, new exam avg: {exam_average:.1f}\n")

    print("Name              HW      Exam    Final")
    for student in gradebook:
        final_grade = (0.4*student[HW_INDEX] + 0.6*student[EXAM_INDEX])
        print(f"{student[NAME_INDEX]:<15}{student[HW_INDEX]:>8.1f}"
              f"{student[EXAM_INDEX]:>8.1f}{final_grade:>8.1f}")


def curve_exams(records, curve):
    """
    Mutate each inner list so its exam score is increased by `curve`
    points without exceeding 100.

    Parameters
        records: compound list (list of [name, hw, exam])
        curve:   amount to add to each exam score
    """
    # Loop through each inner list and adjust the EXAM_INDEX element.
    for record in records:
        record[EXAM_INDEX] += curve

        # Final score cannot be more than 100
        record[EXAM_INDEX] = min(record[EXAM_INDEX], 100)


def compute_averages(gradebook):
    """
    Compute average scores in gradebook.

    Parameters
        gradebook (list): list of student names and scores

    Returns
        tuple: (homework average, exam average, top student name, top exam)
    """
    exam_total = 0
    hw_total = 0
    top_exam = gradebook[0][EXAM_INDEX]  # First student's exam
    top_student = gradebook[0][NAME_INDEX]  # First student's name
    for student in gradebook:
        exam_total += student[EXAM_INDEX]
        hw_total += student[HW_INDEX]
        if student[EXAM_INDEX] > top_exam:
            top_exam = student[EXAM_INDEX]
            top_student = student[NAME_INDEX]

    hw_average = hw_total/len(gradebook)
    exam_average = exam_total/len(gradebook)

    return hw_average, exam_average, top_student, top_exam


# Run the program
if __name__ == "__main__":
    main()
