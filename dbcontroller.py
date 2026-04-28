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
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def update_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

# Course
def add_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def delete_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def update_course():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

# Instructor
def add_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def delete_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def update_instructor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def get_all_sections():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def get_all_enrollments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)

def enroll_student():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)

def update_grade():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()

def delete_enrollment(enrollment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        # sql query goes here
    """)
    conn.commit()
    conn.close()