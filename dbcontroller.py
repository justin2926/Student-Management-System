import sqlite3
from pathlib import Path
from database import *
from main import *

DB_NAME = "student_management.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.StudentID, s.FirstName, s.LastName, s.Major, d.Department
        FROM Students s
        JOIN Departments d ON s.DepartmentID = d.DepartmentID
        ORDER BY s.StudentID
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Student
def add_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Students (FirstName, LastName, Major, DepartmentID)
        VALUES (?, ?, ?, ?)
    """, (student_first_entry.get(), student_last_entry.get(), student_major_entry.get(), student_department_entry.get()))
    conn.commit()
    conn.close()

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Students WHERE StudentID = ?
    """, (student_id_entry.get(),))
    conn.commit()
    conn.close()

def update_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Students SET FirstName = ?, LastName = ?, Major = ? WHERE StudentID = ?
    """, (student_first_entry.get(), student_last_entry.get(), student_major_entry.get(), student_id_entry.get()))
    conn.commit()
    conn.close()

# Course
def add_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Courses (CourseID, DepartmentID, CourseName, Credits) VALUES (?, ?, ?, ?)
    """, (course_id_entry.get(), department_id_entry.get(), course_name_entry.get(), credits_entry.get()))
    conn.commit()
    conn.close()

def delete_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Courses WHERE CourseID = ?
    """, (course_id_entry.get(),))
    conn.commit()
    conn.close()

def update_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Courses SET DepartmentID = ?, CourseName = ?, Credits = ? WHERE CourseID = ?
    """, (department_id_entry.get(), course_name_entry.get(), credits_entry.get(), course_id_entry.get()))
    conn.commit()
    conn.close()

# Instructor
def add_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Instructor (InstructorID, DepartmentID, FirstName, LastName) VALUES (?, ?, ?, ?)
    """, (instructor_id_entry.get(), instructor_department_id_entry.get(), instructor_first_entry.get(), instructor_last_entry.get()))
    conn.commit()
    conn.close()

def delete_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Instructor WHERE InstructorID = ?
    """, (instructor_id_entry.get(),))
    conn.commit()
    conn.close()

def update_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Instructor SET DepartmentID = ?, FirstName = ?, LastName = ? WHERE InstructorID = ?
    """, (instructor_department_id_entry.get(), instructor_first_entry.get(), instructor_last_entry.get(), instructor_id_entry.get()))
    conn.commit()
    conn.close()

def get_all_sections():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Teaches
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM Enrolls
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def enroll_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Enrolls (EnrollmentID, CourseID, StudentID, Grade) VALUES (?, ?, ?, ?)
    """, (enrollment_id_entry.get(), enrollment_course_id_entry.get(), enrollment_student_id_entry.get(), grade_entry.get()))
    conn.commit()
    conn.close()
    
def update_grade():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Enrolls SET Grade = ? WHERE EnrollmentID = ?
    """, (grade_entry.get(), enrollment_id_entry.get()))
    conn.commit()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Enrolls WHERE EnrollmentID = ?
    """, (enrollment_id,))
    conn.commit()
    conn.close()