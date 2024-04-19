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
## Marks Management System

This project implements a Marks Management System in Python for schools. It allows teachers to manage student records and marks for various subjects, while students can view their own marks.

### Features

* **Add Student (Teacher):** Teachers can add new students to the system, entering their names and marks for each subject.
* **Edit Marks (Teacher):** Teachers can edit the marks for specific subjects of existing students.
* **Delete Student (Teacher):** Teachers have the authority to remove a student's record from the system entirely.
* **Display Sorted Marks (Teacher & Student):** Both teachers and students can access a list of all students' total marks sorted in descending order.
* **View Marks (Student):** Students can only view their own marks in all subjects.

### How to Use

1. **Clone the Repository:**
   Use Git to clone this repository to your local machine:

   ```bash
   git clone https://<repository_url>

    
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
