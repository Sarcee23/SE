<h1>College Software Engineering Assignment 4</h1>

There are <b>three</b> programs for the following three questions:

<h2>Assignment 1: Shop Inventory Management System</h2>
# Inventory Management System

This project implements a basic inventory management system with buyer and seller functionalities. It utilizes Python and leverages CSV files for data persistence.

## Features

* **User Management:** Allows users to identify themselves as buyers or sellers.
* **Product Management (Seller):**
    * View product listings with details (ID, name, price, quantity).
    * Restock existing products by adding quantity.
    * Update product prices.
    * Add new products with unique IDs, names, prices, and quantities.
* **Product Interaction (Buyer):**
    * View product listings with details.
    * Purchase products by specifying ID and quantity (subject to stock availability).

## Requirements

* Python 3.x (https://www.python.org/downloads/)
* `csv` module (included in standard library)
* `subprocess` module (included in standard library)  # For Git integration (optional)

## Installation

1. Clone this repository or download the code files.
2. Install any additional required libraries using `pip install <library_name>`.

## Usage

1. Run the `main.py` script:

   ```bash
   python main.py

<h2>Assignment 2: Marks Management System</h2>
Features:
Add Student: Teachers can add new students to the system along with their marks for each subject. Students can also view their own marks.
Edit Marks: Teachers can edit marks for specific subjects of a student. Students have access only to view marks.
Delete Student: Teachers can remove a student's record from the system.
Display Sorted Marks: Both teachers and students can view the marks of all students sorted by total marks in descending order.
How to Use:
Clone the Repository: Clone this repository to your local machine using git clone <repository-url>.

Run the Program: Execute the Python script marks_management.py using a Python interpreter.

Choose Role: Upon running the program, you will be prompted to select your role as a teacher or a student.

Teacher Role: If you choose the teacher role, you will be asked to specify the subject you teach. You can then perform actions such as adding students, editing marks, deleting students, and viewing sorted marks.

Student Role: If you choose the student role, you can only view the sorted marks.

File Structure:
marks_management.py: The main Python script containing the Marks Management System.
marks.csv: CSV file used to store student marks.
Marks_history.txt: Text file used to log changes made to student records.
README.md: Markdown file containing instructions and information about the program.
Dependencies:
Python 3.x
No additional Python packages required.
    
<h2>Assignment 3: Task Management System</h2>
# Task Management System

This project implements a command-line task management system in C++. It allows users to create, edit, mark tasks as complete, view all tasks, delete tasks, and save changes to a CSV file.

## Features

* Add new tasks.
* Edit existing tasks (name only, cannot edit completed tasks).
* Mark tasks as complete.
* View a list of all tasks.
* Delete tasks.
* Save changes to a CSV file.

## Requirements

* C++ compiler (e.g., GCC, Clang)
* Standard C++ libraries (`fstream`, `<vector>`, `<algorithm>`, `<string>`, `<sstream>`, `<limits>`, `<iomanip>`)

## Usage

1. **Compile the code:**

   ```bash
   g++ -o task_manager task_manager.cpp


All of these programs are CLI menu-based, and all of them keep a track of changes as asked for in the question
