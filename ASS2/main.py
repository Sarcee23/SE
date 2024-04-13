import csv
from datetime import datetime

# Constants
MARKS_FILE = 'marks.csv'
HISTORY_FILE = 'Marks_history.txt'
SUBJECTS = ['OOS', 'SE', 'GT', 'GGM', 'CN']  # Updated subjects

def read_marks():
    """Reads marks from the CSV file."""
    with open(MARKS_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_marks(data):
    """Writes marks to the CSV file."""
    with open(MARKS_FILE, mode='w', newline='') as file:
        if data:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        else:
            # If data is empty, write an empty file with just the headers
            writer = csv.DictWriter(file, fieldnames=['Name', 'Roll Number'] + SUBJECTS)
            writer.writeheader()

def log_change(action, details):
    """Logs changes to the history file."""
    with open(HISTORY_FILE, mode='a', newline='') as file:
        file.write(f"{datetime.now()} - {action}: {details}\n")

def validate_mark(mark):
    """Validates that the mark is within the range 0 to 100."""
    try:
        mark = int(mark)
        if 0 <= mark <= 100:
            return mark
        else:
            raise ValueError
    except ValueError:
        print("Invalid mark. Please enter a value between 0 and 100.")
        return validate_mark(input("Re-enter the mark: "))

def add_student(teacher_subject=None):
    """Adds a new student's marks."""
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    marks = {subject: validate_mark(input(f"Enter marks for {subject}: ")) if not teacher_subject or subject == teacher_subject else '0' for subject in SUBJECTS}
    new_student = {'Name': name, 'Roll Number': roll_number, **marks}
    marks_data.append(new_student)
    write_marks(marks_data)
    log_change("Added", new_student)

def edit_marks(teacher_subject):
    """Edits marks for a specific student and subject."""
    roll_number = input("Enter the roll number of the student: ")
    subject = input("Enter the subject to edit marks for: ")
    if subject in SUBJECTS and (not teacher_subject or subject == teacher_subject):
        new_mark = validate_mark(input("Enter the new mark: "))
        for student in marks_data:
            if student['Roll Number'] == roll_number:
                old_mark = student[subject]
                student[subject] = new_mark
                write_marks(marks_data)
                log_change("Edited", f"Roll Number: {roll_number}, Subject: {subject}, Old Mark: {old_mark}, New Mark: {new_mark}")
                break
    else:
        print("Invalid subject or access denied.")

def delete_student():
    """Deletes a student's record."""
    roll_number = input("Enter the roll number of the student to delete: ")
    global marks_data
    marks_data = [student for student in marks_data if student['Roll Number'] != roll_number]
    write_marks(marks_data)
    log_change("Deleted", f"Roll Number: {roll_number}")

def display_sorted_marks():
    """Displays marks sorted by total in a table format."""
    print("\n{:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Roll No', 'Name', *SUBJECTS, 'Total'))
    sorted_data = sorted(marks_data, key=lambda x: sum(int(x[sub]) for sub in SUBJECTS), reverse=True)
    for student in sorted_data:
        total_marks = sum(int(student[sub]) for sub in SUBJECTS)
        print("{:<10} {:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(student['Roll Number'], student['Name'], *[student[sub] for sub in SUBJECTS], total_marks))

# Initial setup
marks_data = read_marks()

# Determine user role
role_input = input("Are you a 'teacher' (t) or a 'student' (s)? ").lower()
role = 'teacher' if role_input == 't' else 'student' if role_input == 's' else None
teacher_subject = None
if role == 'teacher':
    teacher_subject = input("Which subject do you teach? (OOS, CN, GT, GGM, SE): ").upper()
    if teacher_subject not in SUBJECTS:
        print("Invalid subject. Exiting...")
        exit()

# Main menu
while True:
    if role == 'teacher':
        print("\n1. Add Student\n2. Edit Marks\n3. Delete Student\n4. Display Sorted Marks\n5. Exit")
        actions = {
            '1': lambda: add_student(teacher_subject),
            '2': lambda: edit_marks(teacher_subject),
            '3': delete_student,
            '4': display_sorted_marks
        }
    elif role == 'student':
        print("\n1. Display Sorted Marks\n2. Exit")
        actions = {
            '1': display_sorted_marks
        }

    choice = input("Enter your choice: ")
    if choice == '2' and role == 'student' or choice == '5' and role == 'teacher':
        print("Exiting...")
        break
    action = actions.get(choice)
    if action:
        action()
    else:
        print("Please enter a valid choice.")