import tkinter as tk
from tkinter import ttk
from database import *

root = tk.Tk()
root.title("Student Management System")
root.geometry("700x500+550+150") 

title = ttk.Label(root, text="Student Management System", font=("Arial", 24))
title.pack(padx=20, pady=20)

# tabs for students, courses, instructors, enrollments
tabControl = ttk.Notebook(root)

students_tab = ttk.Frame(tabControl)
courses_tab = ttk.Frame(tabControl)
instructors_tab = ttk.Frame(tabControl)
enrollments_tab = ttk.Frame(tabControl)
teaches_tab = ttk.Frame(tabControl)

tabControl.add(students_tab, text='Students')
tabControl.add(courses_tab, text='Courses')
tabControl.add(instructors_tab, text='Instructors')
tabControl.add(enrollments_tab, text='Enrollments')
tabControl.add(teaches_tab, text='Teaches')

# added 
overview_tab = ttk.Frame(tabControl)
tabControl.add(overview_tab, text="Overview")

tabControl.pack(expand=1, fill="both")

s = ttk.Style(root)
s.configure("TNotebook", tabposition='n')

# students tab
students_table = ttk.Treeview(students_tab, columns=("student_id", "first_name", "last_name", "major"), show="headings", height=10)

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
student_first_label.place(x=30, y=30)

student_first_entry = tk.StringVar()
student_first = ttk.Entry(students_tab, textvariable=student_first_entry, width=20)
student_first.place(x=110, y=27)

student_last_label = ttk.Label(students_tab, text="Last Name:")
student_last_label.place(x=30, y=73)

student_last_entry = tk.StringVar()
student_last = ttk.Entry(students_tab, textvariable=student_last_entry, width=20)
student_last.place(x=110, y=70)

student_id_label = ttk.Label(students_tab, text="Student ID:")
student_id_label.place(x=365, y=73)

student_id_entry = tk.StringVar()
student_id = ttk.Entry(students_tab, textvariable=student_id_entry, width=20)
student_id.place(x=440, y=70)

major_label = ttk.Label(students_tab, text="Major:")
major_label.place(x=395, y=30)

major_entry = tk.StringVar()
major = ttk.Entry(students_tab, textvariable=major_entry, width=20)
major.place(x=440, y=27)

def handle_add_student():
    add_student(student_id_entry.get(), student_first_entry.get(), student_last_entry.get(), major_entry.get())

    student_first_entry.set("")
    student_last_entry.set("")
    student_id_entry.set("")
    major_entry.set("")

    refresh_students_table()
    refresh_overview_table()

add_student_button = ttk.Button(students_tab, text="Add Student", command=handle_add_student)
add_student_button.place(x=120, y=110)

def handle_delete_student():
    delete_student(student_id_entry.get())

    student_id_entry.set("")

    refresh_students_table()
    refresh_overview_table()

delete_student_button = ttk.Button(students_tab, text="Delete Student", command=handle_delete_student)
delete_student_button.place(x=250, y=110)

def handle_update_student():
    update_student(student_id_entry.get(), student_first_entry.get(), student_last_entry.get(), major_entry.get())
    refresh_students_table()
    refresh_overview_table()

update_student_button = ttk.Button(students_tab, text="Update Student", command=handle_update_student)
update_student_button.place(x=395, y=110)

# courses tab
courses_table = ttk.Treeview(courses_tab, columns=("course_id", "department_id", "course_name", "credits"), show="headings", height=10)

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
course_id_label.place(x=30, y=30)

course_id_entry = tk.StringVar()
course_id = ttk.Entry(courses_tab, textvariable=course_id_entry, width=20)
course_id.place(x=110, y=27)

department_id_label = ttk.Label(courses_tab, text="Department ID:")
department_id_label.place(x=10, y=73)

department_id_entry = tk.StringVar()
department_id = ttk.Entry(courses_tab, textvariable=department_id_entry, width=20)
department_id.place(x=110, y=70)

course_name_label = ttk.Label(courses_tab, text="Course Name:")
course_name_label.place(x=345, y=73)

course_name_entry = tk.StringVar()
course_name = ttk.Entry(courses_tab, textvariable=course_name_entry, width=20)
course_name.place(x=440, y=70)

credits_label = ttk.Label(courses_tab, text="Credits:")
credits_label.place(x=385, y=30)

credits_entry = tk.StringVar()
credits = ttk.Entry(courses_tab, textvariable=credits_entry, width=20)
credits.place(x=440, y=27)

def handle_add_course():
    add_course(course_id_entry.get(), department_id_entry.get(), course_name_entry.get(), credits_entry.get())
    refresh_courses_table()
    refresh_overview_table()

add_course_button = ttk.Button(courses_tab, text="Add Course", command=handle_add_course)
add_course_button.place(x=120, y=110)

def handle_delete_course():
    delete_course(course_id_entry.get())
    refresh_courses_table()
    refresh_overview_table()

delete_course_button = ttk.Button(courses_tab, text="Delete Course", command=handle_delete_course)
delete_course_button.place(x=250, y=110)

def handle_update_course():
    update_course(course_id_entry.get(), department_id_entry.get(), course_name_entry.get(), credits_entry.get())
    refresh_courses_table()
    refresh_overview_table()

update_course_button = ttk.Button(courses_tab, text="Update Course", command=handle_update_course)
update_course_button.place(x=395, y=110)

# instructors tab
instructors_table = ttk.Treeview(instructors_tab, columns=("instructor_id", "department_id", "first_name", "last_name"), show="headings", height=10)

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
instructor_id_label.place(x=20, y=30)

instructor_id_entry = tk.StringVar()
instructor_id = ttk.Entry(instructors_tab, textvariable=instructor_id_entry, width=20)
instructor_id.place(x=110, y=27)

instructor_department_id_label = ttk.Label(instructors_tab, text="Department ID:")
instructor_department_id_label.place(x=10, y=73)

instructor_department_id_entry = tk.StringVar()
instructor_department_id = ttk.Entry(instructors_tab, textvariable=instructor_department_id_entry, width=20)
instructor_department_id.place(x=110, y=70)

instructor_first_label = ttk.Label(instructors_tab, text="First Name:")
instructor_first_label.place(x=365, y=73)

instructor_first_entry = tk.StringVar()
instructor_first = ttk.Entry(instructors_tab, textvariable=instructor_first_entry, width=20)
instructor_first.place(x=440, y=70)

instructor_last_label = ttk.Label(instructors_tab, text="Last Name:")
instructor_last_label.place(x=365, y=30)

instructor_last_entry = tk.StringVar()
instructor_last = ttk.Entry(instructors_tab, textvariable=instructor_last_entry, width=20)
instructor_last.place(x=440, y=27)

def handle_add_instructor():
    add_instructor(instructor_id_entry.get(), instructor_department_id_entry.get(), instructor_first_entry.get(), instructor_last_entry.get())
    refresh_instructors_table()
    refresh_overview_table()

add_instructor_button = ttk.Button(instructors_tab, text="Add Instructor", command=handle_add_instructor)
add_instructor_button.place(x=120, y=110)

def handle_delete_instructor():
    delete_instructor(instructor_id_entry.get())
    refresh_instructors_table()
    refresh_overview_table()

delete_instructor_button = ttk.Button(instructors_tab, text="Delete Instructor", command=handle_delete_instructor)
delete_instructor_button.place(x=250, y=110)

def handle_update_instructor():
    update_instructor(instructor_id_entry.get(), instructor_department_id_entry.get(), instructor_first_entry.get(), instructor_last_entry.get())
    refresh_instructors_table()
    refresh_overview_table()

update_instructor_button = ttk.Button(instructors_tab, text="Update Instructor", command=handle_update_instructor)
update_instructor_button.place(x=395, y=110)

# enrollments table
enrollments_table = ttk.Treeview(
    enrollments_tab,
    columns=("enrollment_id", "course_id", "student_id", "grade"),
    show="headings",
    height=10
)

enrollments_table.heading("enrollment_id", text="Enrollment ID")
enrollments_table.column("enrollment_id", width=172, anchor="center")

enrollments_table.heading("course_id", text="Course ID")
enrollments_table.column("course_id", width=172, anchor="center")

enrollments_table.heading("student_id", text="Student ID")
enrollments_table.column("student_id", width=172, anchor="center")

enrollments_table.heading("grade", text="Grade")
enrollments_table.column("grade", width=172, anchor="center")

enrollments_table.place(y=150)

enrollment_id_label = ttk.Label(enrollments_tab, text="Enrollment ID:")
enrollment_id_label.place(x=20, y=30)

enrollment_id_entry = tk.StringVar()
enrollment_id = ttk.Entry(enrollments_tab, textvariable=enrollment_id_entry, width=20)
enrollment_id.place(x=110, y=27)

enrollment_course_id_label = ttk.Label(enrollments_tab, text="Course ID:")
enrollment_course_id_label.place(x=35, y=73)

enrollment_course_id_entry = tk.StringVar()
enrollment_course_id = ttk.Entry(enrollments_tab, textvariable=enrollment_course_id_entry, width=20)
enrollment_course_id.place(x=110, y=70)

enrollment_student_id_label = ttk.Label(enrollments_tab, text="Student ID:")
enrollment_student_id_label.place(x=372, y=30)

enrollment_student_id_entry = tk.StringVar()
enrollment_student_id = ttk.Entry(enrollments_tab, textvariable=enrollment_student_id_entry, width=20)
enrollment_student_id.place(x=440, y=27)

grade_label = ttk.Label(enrollments_tab, text="Grade:")
grade_label.place(x=395, y=73)

grade_entry = tk.StringVar()
grade = ttk.Entry(enrollments_tab, textvariable=grade_entry, width=20)
grade.place(x=440, y=70)

def handle_add_enrollment():
    add_enrollment(enrollment_id_entry.get(), enrollment_course_id_entry.get(), enrollment_student_id_entry.get(), grade_entry.get())
    refresh_enrollments_table()
    refresh_overview_table()

add_enrollment_button = ttk.Button(enrollments_tab, text="Add Enrollment", command=handle_add_enrollment)
add_enrollment_button.place(x=105, y=110)

def handle_delete_enrollment():
    delete_enrollment(enrollment_id_entry.get())
    refresh_enrollments_table()
    refresh_overview_table()

delete_enrollment_button = ttk.Button(enrollments_tab, text="Delete Enrollment", command=handle_delete_enrollment)
delete_enrollment_button.place(x=245, y=110)

def handle_update_enrollment():
    update_enrollment(enrollment_id_entry.get(), enrollment_course_id_entry.get(), enrollment_student_id_entry.get(), grade_entry.get())
    refresh_enrollments_table()
    refresh_overview_table()

update_enrollment_button = ttk.Button(enrollments_tab, text="Update Enrollment", command=handle_update_enrollment)
update_enrollment_button.place(x=395, y=110)

# teaches tab
teaches_table = ttk.Treeview(
    teaches_tab,
    columns=("instructor_id", "course_id"),
    show="headings",
    height=10
)

teaches_table.heading("instructor_id", text="Instructor ID")
teaches_table.column("instructor_id", width=345, anchor="center")

teaches_table.heading("course_id", text="Course ID")
teaches_table.column("course_id", width=345, anchor="center")

teaches_table.place(y=150)

teaches_instructor_id_label = ttk.Label(teaches_tab, text="Instructor ID:")
teaches_instructor_id_label.place(x=20, y=30)

teaches_instructor_id_entry = tk.StringVar()
teaches_instructor_id = ttk.Entry(teaches_tab, textvariable=teaches_instructor_id_entry, width=20)
teaches_instructor_id.place(x=110, y=27)

teaches_course_id_label = ttk.Label(teaches_tab, text="Course ID:")
teaches_course_id_label.place(x=360, y=30)

teaches_course_id_entry = tk.StringVar()
teaches_course_id = ttk.Entry(teaches_tab, textvariable=teaches_course_id_entry, width=20)
teaches_course_id.place(x=440, y=27)

def handle_add_teaches():
    add_teaches(teaches_instructor_id_entry.get(), teaches_course_id_entry.get())
    refresh_teaches_table()
    refresh_overview_table()

add_teaches_button = ttk.Button(teaches_tab, text="Add Teaches", command=handle_add_teaches)
add_teaches_button.place(x=120, y=110)

def handle_delete_teaches():
    delete_teaches(teaches_instructor_id_entry.get(), teaches_course_id_entry.get())
    refresh_teaches_table()
    refresh_overview_table()

delete_teaches_button = ttk.Button(teaches_tab, text="Delete Teaches", command=handle_delete_teaches)
delete_teaches_button.place(x=260, y=110)

def handle_update_teaches():
    update_teaches(teaches_instructor_id_entry.get(), teaches_course_id_entry.get())
    refresh_teaches_table()
    refresh_overview_table()

update_teaches_button = ttk.Button(teaches_tab, text="Update Teaches", command=handle_update_teaches)
update_teaches_button.place(x=400, y=110)

# overview tab
overview_table = ttk.Treeview(
    overview_tab,
    columns=("student_id", "student_name", "course_id", "course_name", "instructor_id", "instructor_name", "major", "grade"),
    show="headings",
    height=15
)

overview_columns = [
    ("student_id", "Student ID", 80),
    ("student_name", "Student Name", 120),
    ("course_id", "Course ID", 80),
    ("course_name", "Course Name", 160),
    ("instructor_id", "Instructor ID", 90),
    ("instructor_name", "Instructor Name", 130),
    ("major", "Major", 130),
    ("grade", "Grade", 60)
]

for col, text, width in overview_columns:
    overview_table.heading(col, text=text)
    overview_table.column(col, width=width, anchor="center")

overview_table.place(x=0, y=30)

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

def refresh_teaches_table():
    for i in teaches_table.get_children():
        teaches_table.delete(i)

    for i in view_teaches():
        teaches_table.insert("", tk.END, values=(i[0], i[1]))

def refresh_overview_table():
    for i in overview_table.get_children():
        overview_table.delete(i)

    for i in view_overview():
        overview_table.insert("", tk.END, values=i)

get_connection()
create_tables()
sample_data_insertion()

refresh_students_table()
refresh_courses_table()
refresh_instructors_table()
refresh_enrollments_table()
refresh_teaches_table()
refresh_overview_table()

root.mainloop()