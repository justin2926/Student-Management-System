import tkinter as tk
from tkinter import ttk
from database import *

root = tk.Tk()
root.title("Student Management System")
root.geometry("700x500+550+150") 

title = ttk.Label(root, text="Student Management System", font=("Arial", 24))
title.pack(padx=20,pady=20)

# tabs for students, courses, instructors, enrollments
tabControl = ttk.Notebook(root)

students_tab = ttk.Frame(tabControl)
courses_tab = ttk.Frame(tabControl)
instructors_tab = ttk.Frame(tabControl)
enrollments_tab = ttk.Frame(tabControl)
departments_tab = ttk.Frame(tabControl)

tabControl.add(students_tab, text='Students')
tabControl.add(courses_tab, text='Courses')
tabControl.add(instructors_tab, text='Instructors')
tabControl.add(enrollments_tab, text='Enrollments')
tabControl.add(departments_tab, text="Departments")

tabControl.pack(expand=1, fill="both")

# students tab
students_table = ttk.Treeview(students_tab, columns=("student_id", "first_name", "last_name", "major"), show = "headings", height=8)

style = ttk.Style()

students_table.heading("student_id", text="Student ID")
students_table.column("student_id", width=75)

students_table.heading("first_name", text="First Name")
students_table.column("first_name", width=75)

students_table.heading("last_name", text="Last Name")
students_table.column("last_name", width=75)

students_table.heading("major", text="Major")
students_table.column("major", width=150)

students_table.place(x=130, y=150)

student_first_label = ttk.Label(students_tab, text="First Name:")
student_first_label.pack(padx=10, pady=2)

student_first_entry = tk.StringVar()
student_first = ttk.Entry(students_tab, textvariable=student_first_entry, width=20)
student_first.pack(padx=10, pady=2)

student_last_label = ttk.Label(students_tab, text="Last Name:")
student_last_label.pack(padx=10, pady=2)

student_last_entry = tk.StringVar()
student_last = ttk.Entry(students_tab, textvariable=student_last_entry, width=20)
student_last.pack(padx=10, pady=2)

# courses tab
courses_table = ttk.Treeview(courses_tab, columns=("course_id", "department_id", "course_name", "credits"), show = "headings", height=8)

style = ttk.Style()

courses_table.heading("course_id", text="Course ID")
courses_table.column("course_id", width=75)

courses_table.heading("department_id", text="Department ID")
courses_table.column("department_id", width=75)

courses_table.heading("course_name", text="Course Name")
courses_table.column("course_name", width=175)

courses_table.heading("credits", text="Credits")
courses_table.column("credits", width=50)

courses_table.place(x=130, y=150)

# instructors tab
instructors_table = ttk.Treeview(instructors_tab, columns=("instructor_id", "department_id", "first_name", "last_name"), show = "headings", height=8)

style = ttk.Style()

instructors_table.heading("instructor_id", text="Instructor ID")
instructors_table.column("instructor_id", width=100)

instructors_table.heading("department_id", text="Department ID")
instructors_table.column("department_id", width=100)

instructors_table.heading("first_name", text="First Name")
instructors_table.column("first_name", width=75)

instructors_table.heading("last_name", text="Last Name")
instructors_table.column("last_name", width=150)

instructors_table.place(x=110, y=150)

# departments tab
departments_table = ttk.Treeview(departments_tab, columns=("department_id", "department_name", "location"), show = "headings", height=8)

style = ttk.Style()

departments_table.heading("department_id", text="Department ID")
departments_table.column("department_id", width=100)

departments_table.heading("department_name", text="Department Name")
departments_table.column("department_name", width=100)

departments_table.heading("location", text="Location")
departments_table.column("location", width=100)

departments_table.place(x=130, y=150)

# enrollments table
enrollments_table = ttk.Treeview(enrollments_tab, columns=("enrollment_id", "course_id", "student_id", "grade"), show = "headings", height=8)

style = ttk.Style()

enrollments_table.heading("enrollment_id", text="Enrollment ID")
enrollments_table.column("enrollment_id", width=75)

enrollments_table.heading("course_id", text="Course ID")
enrollments_table.column("course_id", width=75)

enrollments_table.heading("student_id", text="Student ID")
enrollments_table.column("student_id", width=75)

enrollments_table.heading("grade", text="Grade")
enrollments_table.column("grade", width=150)

enrollments_table.place(x=130, y=150)

def refresh_students_table():
    for i in students_table.get_children():
        students_table.delete(i)

    for i in view_students():
        students_table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

def refresh_courses_table():
    for i in courses_table.get_children():
        courses_table.delete(i)

    for i in view_courses():
        courses_table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

def refresh_instructors_table():
    for i in instructors_table.get_children():
        instructors_table.delete(i)

    for i in view_instructors():
        instructors_table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

# def refresh_departments_table():
#     for i in departments_table.get_children():
#         departments_table.delete(i)

#     for i in view():
#         departments_table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

get_connection()
create_tables()
sample_data_insertion()
refresh_students_table()
refresh_courses_table()
refresh_instructors_table()

root.mainloop()