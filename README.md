# Student Management System

## Project Overview

The **Student Management System** is a desktop-based database application designed to help manage student course registration and academic records.

This system allows school staff to manage:

- Students
- Courses
- Instructors
- Departments
- Student Enrollments
- Course Assignments (Teaches)
- Student Grades

The goal of this project is to provide an organized way to manage academic records while demonstrating real-world database relationships and CRUD (Create, Read, Update, Delete) operations using SQL. The system helps faculty staff manage semester courses, assign instructors to courses, enroll students, and track student grades. 

---

## Technologies Used

This application was developed using:

- **Python** – Application logic and backend processing
- **SQLite3** – Database management system
- **Tkinter** – Graphical User Interface (GUI)
- **Visual Studio Code** – Development environment

The system runs as a desktop application titled **Student Management System** using a tabbed notebook interface. 

---

## Project Structure

```plaintext
Student-Management-System/
│── database.py                  # Database schema and database functions
│── main.py                      # Main GUI application
│── student_management_system.db # SQLite database
│── README.md                    # Project documentation
│── __pycache__/                 # Python cache files
```

---

## Features

The Student Management System supports the following features:

### Student Management
- Add student records
- Update student information
- Delete student records
- View student information

### Course Management
- Add courses
- Update courses
- Delete courses
- View course information

### Instructor Management
- Add instructors
- Update instructor records
- Delete instructors
- View instructor information

### Enrollment Management
- Enroll students in courses
- Update student grades
- Delete enrollments
- Track course enrollment records

### Overview Tab
- Displays:
  - Student ID
  - Student Name
  - Course ID
  - Course Name
  - Instructor ID
  - Instructor Name
  - Major
  - Grade

The system also includes sample data initialization for demonstration purposes. 

---

## Database Design

The database consists of the following tables:

| Table | Purpose |
|--------|----------|
| Department | Stores department information |
| Students | Stores student information |
| Instructor | Stores instructor information |
| Courses | Stores course information |
| Enrolls | Tracks student enrollments |
| Teaches | Tracks instructor course assignments |

Relationships include:

- One student can enroll in many courses
- One course can have many students
- One instructor can teach multiple courses
- One department can offer multiple courses
- Enrolls connects Students and Courses
- Teaches connects Instructors and Courses 

---

## Dependencies / Required Software

Before running the project, make sure you have the following installed:

### Required Software
- **Python 3.12+**
- **Visual Studio Code** (recommended)

### Python Libraries
The following libraries are required:

```python
sqlite3
tkinter
pathlib
```

These libraries are included with Python by default, so no additional installation is required.

---

## Setup Instructions

### 1. Clone the Repository

Open terminal and run:

```bash
git clone https://github.com/justin2926/Student-Management-System.git
```

### 2. Navigate into the Project Folder

```bash
cd Student-Management-System
```

### 3. Open the Project

Open the folder in **Visual Studio Code**.

---

## How to Run the Project

Run the application using:

```bash
python main.py
```

The Student Management System GUI should open.

During startup, the application automatically:

- Connects to the SQLite database
- Creates tables (if they do not exist)
- Inserts sample data

The following functions are called during initialization:

```python
get_connection()
create_tables()
sample_data_insertion()
```

This ensures the database is populated and ready for demonstration. 

---

## Database Configuration

The project uses an SQLite database file:

```plaintext
student_management_system.db
```

No external database setup is required.

SQLite automatically creates the database file when the application runs for the first time.

Foreign key constraints are enabled using:

```python
PRAGMA foreign_keys = ON;
```

---

## Future Improvements

Potential improvements for future versions include:

- User login authentication
- Search and filtering features
- Better duplicate ID validation
- Advanced grade reports
- Student schedule conflict detection
- Web-based version of the system
- Exporting reports to PDF or CSV 

---

## Team Members

- Justin Nguyen  
- Alan Nguyen  
- Thuan Lam   

Course: **CS157A Section 3**  
Instructor: **Dr. Tahereh Arabghalizi** 