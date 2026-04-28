import sqlite3

DATABASE_NAME = "student_management_system.db"


def get_connection():
    con = sqlite3.connect(DATABASE_NAME)
    con.execute("PRAGMA foreign_keys = ON")
    return con

# creating tables
def create_tables():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            DepartmentID INTEGER PRIMARY KEY,
            DepartmentName TEXT NOT NULL,
            Location TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Major TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Instructor (
            InstructorID INTEGER PRIMARY KEY,
            DepartmentID INTEGER NOT NULL,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY,
            DepartmentID INTEGER NOT NULL,
            CourseName TEXT NOT NULL,
            Credits INTEGER NOT NULL,
            FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Enrolls (
            EnrollmentID INTEGER PRIMARY KEY,
            CourseID INTEGER NOT NULL,
            StudentID INTEGER NOT NULL,
            Grade TEXT NOT NULL,
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
            FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
            UNIQUE (CourseID, StudentID)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Teaches (
            InstructorID INTEGER NOT NULL,
            CourseID INTEGER NOT NULL,
            PRIMARY KEY (InstructorID, CourseID),
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID),
            FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        )
    """)

    con.commit()
    con.close()

# inserting sample data
def sample_data_insertion():
    con = get_connection()
    cur = con.cursor()

    departments = [
        (1, "Computer Science", "MacQuarrie Hall"),
        (2, "Mathematics", "Duncan Hall"),
        (3, "Biology", "Science Building"),
        (4, "Business", "Business Tower"),
        (5, "Engineering", "Engineering Building"),
        (6, "English", "Faculty Offices"),
        (7, "History", "Clark Hall"),
        (8, "Physics", "Science Building"),
        (9, "Chemistry", "Science Building"),
        (10, "Art", "Art Building"),
        (11, "Music", "Music Building"),
        (12, "Psychology", "Dudley Moorhead Hall"),
        (13, "Sociology", "Clark Hall"),
        (14, "Kinesiology", "Spartan Complex"),
        (15, "Education", "Sweeney Hall")
    ]

    students = [
        (1001, "Alan", "Nguyen", "Computer Science"),
        (1002, "Justin", "Nguyen", "Computer Science"),
        (1003, "Thuan", "Lam", "Computer Science"),
        (1004, "Emily", "Tran", "Business"),
        (1005, "David", "Kim", "Engineering"),
        (1006, "Sophia", "Lee", "Biology"),
        (1007, "Michael", "Chen", "Mathematics"),
        (1008, "Sarah", "Garcia", "Psychology"),
        (1009, "Daniel", "Patel", "Physics"),
        (1010, "Olivia", "Brown", "English"),
        (1011, "James", "Wilson", "History"),
        (1012, "Mia", "Martinez", "Chemistry"),
        (1013, "Ethan", "Davis", "Art"),
        (1014, "Ava", "Lopez", "Music"),
        (1015, "Noah", "Taylor", "Education")
    ]

    instructors = [
        (2001, 1, "John", "Smith"),
        (2002, 2, "Mary", "Johnson"),
        (2003, 3, "Robert", "Williams"),
        (2004, 4, "Patricia", "Brown"),
        (2005, 5, "Michael", "Jones"),
        (2006, 6, "Linda", "Garcia"),
        (2007, 7, "William", "Miller"),
        (2008, 8, "Elizabeth", "Davis"),
        (2009, 9, "David", "Rodriguez"),
        (2010, 10, "Jennifer", "Martinez"),
        (2011, 11, "Richard", "Hernandez"),
        (2012, 12, "Susan", "Lopez"),
        (2013, 13, "Joseph", "Gonzalez"),
        (2014, 14, "Karen", "Wilson"),
        (2015, 15, "Thomas", "Anderson")
    ]

    courses = [
        (3001, 1, "Database Management Systems", 3),
        (3002, 1, "Data Structures", 3),
        (3003, 2, "Calculus I", 4),
        (3004, 3, "General Biology", 4),
        (3005, 4, "Introduction to Business", 3),
        (3006, 5, "Engineering Design", 3),
        (3007, 6, "English Composition", 3),
        (3008, 7, "World History", 3),
        (3009, 8, "General Physics", 4),
        (3010, 9, "General Chemistry", 4),
        (3011, 10, "Drawing Fundamentals", 3),
        (3012, 11, "Music Theory", 3),
        (3013, 12, "Intro to Psychology", 3),
        (3014, 13, "Intro to Sociology", 3),
        (3015, 15, "Foundations of Education", 3)
    ]

    enrolls = [
        (1, 3001, 1001, "A"),
        (2, 3001, 1002, "B"),
        (3, 3002, 1003, "A"),
        (4, 3003, 1004, "B"),
        (5, 3004, 1005, "C"),
        (6, 3005, 1006, "A"),
        (7, 3006, 1007, "B"),
        (8, 3007, 1008, "A"),
        (9, 3008, 1009, "B"),
        (10, 3009, 1010, "C"),
        (11, 3010, 1011, "A"),
        (12, 3011, 1012, "B"),
        (13, 3012, 1013, "A"),
        (14, 3013, 1014, "B"),
        (15, 3014, 1015, "A")
    ]

    teaches = [
        (2001, 3001),
        (2001, 3002),
        (2002, 3003),
        (2003, 3004),
        (2004, 3005),
        (2005, 3006),
        (2006, 3007),
        (2007, 3008),
        (2008, 3009),
        (2009, 3010),
        (2010, 3011),
        (2011, 3012),
        (2012, 3013),
        (2013, 3014),
        (2015, 3015)
    ]

    cur.executemany("INSERT OR IGNORE INTO Department VALUES (?, ?, ?)", departments)
    cur.executemany("INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?)", students)
    cur.executemany("INSERT OR IGNORE INTO Instructor VALUES (?, ?, ?, ?)", instructors)
    cur.executemany("INSERT OR IGNORE INTO Courses VALUES (?, ?, ?, ?)", courses)
    cur.executemany("INSERT OR IGNORE INTO Enrolls VALUES (?, ?, ?, ?)", enrolls)
    cur.executemany("INSERT OR IGNORE INTO Teaches VALUES (?, ?)", teaches)

    con.commit()
    con.close()
    

def view_students():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Students")
    rows = cur.fetchall()

    con.close()
    return rows


def add_student(student_id, first_name, last_name, major):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Students (StudentID, FirstName, LastName, Major)
        VALUES (?, ?, ?, ?)
    """, (student_id, first_name, last_name, major))

    con.commit()
    con.close()


def update_student(student_id, first_name, last_name, major):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE Students
        SET FirstName = ?, LastName = ?, Major = ?
        WHERE StudentID = ?
    """, (first_name, last_name, major, student_id))

    con.commit()
    con.close()


def delete_student(student_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))

    con.commit()
    con.close()


def test_database():
    create_tables()
    sample_data_insertion()
    print("The database and sample data have been successfully created!")


if __name__ == "__main__":
    test_database()


# CRUD Functions for Courses, Instructor, Enrolls _______________________________________________________________________

# Course 
def view_courses():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Courses")
    rows = cur.fetchall()

    con.close()
    return rows


def add_course(course_id, department_id, course_name, credits):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Courses (CourseID, DepartmentID, CourseName, Credits)
        VALUES (?, ?, ?, ?)
    """, (course_id, department_id, course_name, credits))

    con.commit()
    con.close()


def update_course(course_id, department_id, course_name, credits):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE Courses
        SET DepartmentID = ?, CourseName = ?, Credits = ?
        WHERE CourseID = ?
    """, (department_id, course_name, credits, course_id))

    con.commit()
    con.close()


def delete_course(course_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM Courses WHERE CourseID = ?", (course_id,))

    con.commit()
    con.close()


# Instructor__________________________________________________________________________ 

def view_instructors():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Instructor")
    rows = cur.fetchall()

    con.close()
    return rows


def add_instructor(instructor_id, department_id, first_name, last_name):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Instructor (InstructorID, DepartmentID, FirstName, LastName)
        VALUES (?, ?, ?, ?)
    """, (instructor_id, department_id, first_name, last_name))

    con.commit()
    con.close()


def update_instructor(instructor_id, department_id, first_name, last_name):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE Instructor
        SET DepartmentID = ?, FirstName = ?, LastName = ?
        WHERE InstructorID = ?
    """, (department_id, first_name, last_name, instructor_id))

    con.commit()
    con.close()


def delete_instructor(instructor_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM Instructor WHERE InstructorID = ?", (instructor_id,))

    con.commit()
    con.close()


# Enrolls__________________________________________________________________________________

def view_enrollments():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Enrolls")
    rows = cur.fetchall()

    con.close()
    return rows


def add_enrollment(enrollment_id, course_id, student_id, grade):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Enrolls (EnrollmentID, CourseID, StudentID, Grade)
        VALUES (?, ?, ?, ?)
    """, (enrollment_id, course_id, student_id, grade))

    con.commit()
    con.close()


def update_enrollment(enrollment_id, course_id, student_id, grade):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE Enrolls
        SET CourseID = ?, StudentID = ?, Grade = ?
        WHERE EnrollmentID = ?
    """, (course_id, student_id, grade, enrollment_id))

    con.commit()
    con.close()


def delete_enrollment(enrollment_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM Enrolls WHERE EnrollmentID = ?", (enrollment_id,))

    con.commit()
    con.close()


def view_teaches():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Teaches")
    rows = cur.fetchall()

    con.close()
    return rows


def add_teaches(instructor_id, course_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Teaches (InstructorID, CourseID)
        VALUES (?, ?)
    """, (instructor_id, course_id))

    con.commit()
    con.close()

# Teaches

def update_teaches(old_instructor_id, old_course_id, new_instructor_id, new_course_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        UPDATE Teaches
        SET InstructorID = ?, CourseID = ?
        WHERE InstructorID = ? AND CourseID = ?
    """, (new_instructor_id, new_course_id, old_instructor_id, old_course_id))

    con.commit()
    con.close()


def delete_teaches(instructor_id, course_id):
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        DELETE FROM Teaches
        WHERE InstructorID = ? AND CourseID = ?
    """, (instructor_id, course_id))

    con.commit()
    con.close()

    # Some Join Queries_______________________________________________________________

# query 1
def view_student_grades():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT
            Students.StudentID,
            Students.FirstName,
            Students.LastName,
            Courses.CourseName,
            Enrolls.Grade
        FROM Enrolls
        JOIN Students
            ON Enrolls.StudentID = Students.StudentID
        JOIN Courses
            ON Enrolls.CourseID = Courses.CourseID
    """)

    rows = cur.fetchall()

    con.close()
    return rows

# query 2
def view_instructor_courses():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT
            Instructor.FirstName,
            Instructor.LastName,
            Courses.CourseName
        FROM Teaches
        JOIN Instructor
            ON Teaches.InstructorID = Instructor.InstructorID
        JOIN Courses
            ON Teaches.CourseID = Courses.CourseID
    """)

    rows = cur.fetchall()

    con.close()
    return rows

# added another join query
def view_overview():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
        SELECT
            Students.StudentID,
            Students.FirstName || ' ' || Students.LastName AS StudentName,
            Courses.CourseID,
            Courses.CourseName,
            Instructor.InstructorID,
            Instructor.FirstName || ' ' || Instructor.LastName AS InstructorName,
            Students.Major,
            Enrolls.Grade
        FROM Enrolls
        JOIN Students ON Enrolls.StudentID = Students.StudentID
        JOIN Courses ON Enrolls.CourseID = Courses.CourseID
        LEFT JOIN Teaches ON Courses.CourseID = Teaches.CourseID
        LEFT JOIN Instructor ON Teaches.InstructorID = Instructor.InstructorID
    """)

    rows = cur.fetchall()
    con.close()
    return rows