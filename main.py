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

s = ttk.Style(root)
s.configure("TNotebook", tabposition='n')

# students tab
students_table = ttk.Treeview(students_tab, columns=("student_id", "first_name", "last_name", "major"), show = "headings", height=10)

style = ttk.Style()

students_table.heading("student_id", text="Student ID")
students_table.column("student_id", width=172, anchor="center")

students_table.heading("first_name", text="First Name")
students_table.column("first_name", width=172, anchor="center")

students_table.heading("last_name", text="Last Name")
students_table.column("last_name", width=172, anchor="center")

students_table.heading("major", text="Major")
students_table.column("major", width=172, anchor="center")

students_table.place(y=150)

student_first_label = ttk.Label(students_tab, text="First Name:")
student_first_label.pack(padx=10, pady=2)
student_first_label.place(x=30, y=30)

student_first_entry = tk.StringVar()
student_first = ttk.Entry(students_tab, textvariable=student_first_entry, width=20)
student_first.pack(padx=10, pady=2)
student_first.place(x=110, y=27)

student_last_label = ttk.Label(students_tab, text="Last Name:")
student_last_label.pack(side="left", padx=10, pady=2)
student_last_label.place(x=30, y=73)

student_last_entry = tk.StringVar()
student_last = ttk.Entry(students_tab, textvariable=student_last_entry, width=20)
student_last.pack(side="left", padx=10, pady=2)
student_last.place(x=110, y=70)

student_id_label = ttk.Label(students_tab, text="Student ID:")
student_id_label.pack(side="left", padx=10, pady=2)
student_id_label.place(x=365, y=73)

student_id_entry = tk.StringVar()
student_id = ttk.Entry(students_tab, textvariable=student_id_entry, width=20)
student_id.pack(side="left", padx=10, pady=2)
student_id.place(x=440, y=70)

major_label = ttk.Label(students_tab, text="Major:")
major_label.pack(side="left", padx=10, pady=2)
major_label.place(x=395, y=30)

major_entry = tk.StringVar()
major = ttk.Entry(students_tab, textvariable=major_entry, width=20)
major.pack(side="left", padx=10, pady=2)
major.place(x=440, y=27)

add_student_button = ttk.Button(students_tab, text="Add Student")
add_student_button.pack(padx=10, pady=5)
add_student_button.place(x=120, y=110)

delete_student_button = ttk.Button(students_tab, text="Delete Student")
delete_student_button.pack(padx=10, pady=5)
delete_student_button.place(x=250, y=110)

update_student_button = ttk.Button(students_tab, text="Update Student")
update_student_button.pack(padx=10, pady=5)
update_student_button.place(x=395, y=110)

# courses tab
courses_table = ttk.Treeview(courses_tab, columns=("course_id", "department_id", "course_name", "credits"), show = "headings", height=10)

style = ttk.Style()

courses_table.heading("course_id", text="Course ID")
courses_table.column("course_id", width=172, anchor="center")

courses_table.heading("department_id", text="Department ID")
courses_table.column("department_id", width=172, anchor="center")

courses_table.heading("course_name", text="Course Name")
courses_table.column("course_name", width=172, anchor="center")

courses_table.heading("credits", text="Credits")
courses_table.column("credits", width=172, anchor="center")

courses_table.place(y=150)

course_id_label = ttk.Label(courses_tab, text="Course ID:")
course_id_label.pack(padx=10, pady=2)
course_id_label.place(x=30, y=30)

course_id_entry = tk.StringVar()
course_id = ttk.Entry(courses_tab, textvariable=course_id_entry, width=20)
course_id.pack(padx=10, pady=2)
course_id.place(x=110, y=27)

department_id_label = ttk.Label(courses_tab, text="Department ID:")
department_id_label.pack(side="left", padx=10, pady=2)
department_id_label.place(x=10, y=73)

department_id_entry = tk.StringVar()
department_id = ttk.Entry(courses_tab, textvariable=department_id_entry, width=20)
department_id.pack(side="left", padx=10, pady=2)
department_id.place(x=110, y=70)

course_name_label = ttk.Label(courses_tab, text="Course Name:")
course_name_label.pack(side="left", padx=10, pady=2)
course_name_label.place(x=345, y=73)

course_name_entry = tk.StringVar()
course_name = ttk.Entry(courses_tab, textvariable=course_name_entry, width=20)
course_name.pack(side="left", padx=10, pady=2)
course_name.place(x=440, y=70)

credits_label = ttk.Label(courses_tab, text="Credits:")
credits_label.pack(side="left", padx=10, pady=2)
credits_label.place(x=385, y=30)

credits_entry = tk.StringVar()
credits = ttk.Entry(courses_tab, textvariable=credits_entry, width=20)
credits.pack(side="left", padx=10, pady=2)
credits.place(x=440, y=27)

add_course_button = ttk.Button(courses_tab, text="Add Course")
add_course_button.pack(padx=10, pady=5)
add_course_button.place(x=120, y=110)

delete_course_button = ttk.Button(courses_tab, text="Delete Course")
delete_course_button.pack(padx=10, pady=5)
delete_course_button.place(x=250, y=110)

update_course_button = ttk.Button(courses_tab, text="Update Course")
update_course_button.pack(padx=10, pady=5)
update_course_button.place(x=395, y=110)

# instructors tab
instructors_table = ttk.Treeview(instructors_tab, columns=("instructor_id", "department_id", "first_name", "last_name"), show = "headings", height=10)

style = ttk.Style()

instructors_table.heading("instructor_id", text="Instructor ID")
instructors_table.column("instructor_id", width=172, anchor="center")

instructors_table.heading("department_id", text="Department ID")
instructors_table.column("department_id", width=172, anchor="center")

instructors_table.heading("first_name", text="First Name")
instructors_table.column("first_name", width=172, anchor="center")

instructors_table.heading("last_name", text="Last Name")
instructors_table.column("last_name", width=172, anchor="center")

instructors_table.place(y=150)

instructor_id_label = ttk.Label(instructors_tab, text="Instructor ID:")
instructor_id_label.pack(padx=10, pady=2)
instructor_id_label.place(x=30, y=30)

instructor_id_entry = tk.StringVar()
instructor_id = ttk.Entry(instructors_tab, textvariable=instructor_id_entry, width=20)
instructor_id.pack(padx=10, pady=2)
instructor_id.place(x=110, y=27)

department_id_label = ttk.Label(instructors_tab, text="Department ID:")
department_id_label.pack(side="left", padx=10, pady=2)
department_id_label.place(x=10, y=73)

department_id_entry = tk.StringVar()
department_id = ttk.Entry(instructors_tab, textvariable=department_id_entry, width=20)
department_id.pack(side="left", padx=10, pady=2)
department_id.place(x=110, y=70)

instructor_first_label = ttk.Label(instructors_tab, text="First Name:")
instructor_first_label.pack(side="left", padx=10, pady=2)
instructor_first_label.place(x=345, y=73)

instructor_first_entry = tk.StringVar()
instructor_first = ttk.Entry(instructors_tab, textvariable=instructor_first_entry, width=20)
instructor_first.pack(side="left", padx=10, pady=2)
instructor_first.place(x=440, y=70)

instructor_last_label = ttk.Label(instructors_tab, text="Last Name:")
instructor_last_label.pack(side="left", padx=10, pady=2)
instructor_last_label.place(x=385, y=30)

instructor_last_entry = tk.StringVar()
instructor_last = ttk.Entry(instructors_tab, textvariable=credits_entry, width=20)
instructor_last.pack(side="left", padx=10, pady=2)
instructor_last.place(x=440, y=27)

add_instructor_button = ttk.Button(instructors_tab, text="Add Instructor")
add_instructor_button.pack(padx=10, pady=5)
add_instructor_button.place(x=120, y=110)

delete_instructor_button = ttk.Button(instructors_tab, text="Delete Instructor")
delete_instructor_button.pack(padx=10, pady=5)
delete_instructor_button.place(x=250, y=110)

update_instructor_button = ttk.Button(instructors_tab, text="Update Instructor")
update_instructor_button.pack(padx=10, pady=5)
update_instructor_button.place(x=395, y=110)

# departments tab
departments_table = ttk.Treeview(departments_tab, columns=("department_id", "department_name", "location"), show = "headings", height=10)

style = ttk.Style()

departments_table.heading("department_id", text="Department ID")
departments_table.column("department_id", width=233, anchor="center")

departments_table.heading("department_name", text="Department Name")
departments_table.column("department_name", width=233, anchor="center")

departments_table.heading("location", text="Location")
departments_table.column("location", width=233, anchor="center")

departments_table.place(y=150)

# enrollments table
enrollments_table = ttk.Treeview(enrollments_tab, columns=("enrollment_id", "course_id", "student_id", "grade"), show = "headings", height=10)

style = ttk.Style()

enrollments_table.heading("enrollment_id", text="Enrollment ID")
enrollments_table.column("enrollment_id", width=172, anchor="center")

enrollments_table.heading("course_id", text="Course ID")
enrollments_table.column("course_id", width=172, anchor="center")

enrollments_table.heading("student_id", text="Student ID")
enrollments_table.column("student_id", width=172, anchor="center")

enrollments_table.heading("grade", text="Grade")
enrollments_table.column("grade", width=172, anchor="center")

enrollments_table.place(y=150)

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

def refresh_enrollments_table():
    for i in enrollments_table.get_children():
        enrollments_table.delete(i)

    for i in view_enrollments():
        enrollments_table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

get_connection()
create_tables()
sample_data_insertion()

refresh_students_table()
refresh_courses_table()
refresh_instructors_table()
refresh_enrollments_table()

root.mainloop()