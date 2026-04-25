import tkinter as tk
from tkinter import ttk
from database import *

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x400+550+150") 

title = ttk.Label(root, text="Student Management System", font=("Arial", 24))
title.pack(padx=20,pady=20)

# students_button = ttk.Button(root, text="View Students")
# students_button.place(x=230, y=80)

# courses_button = ttk.Button(root, text="View Courses")
# courses_button.place(x=230, y=130)

# instructor_button = ttk.Button(root, text="View Instructors")
# instructor_button.place(x=230, y=200)

# department_button = ttk.Button(root, text="View Departments")
# department_button.place(x=230, y=300)

# treeview
table = ttk.Treeview(root, columns=("student_id", "first_name", "last_name", "major"), show = "headings", height=8)

style = ttk.Style()

table.heading("student_id", text="Student ID")
table.column("student_id", width=75)

table.heading("first_name", text="First Name")
table.column("first_name", width=75)

table.heading("last_name", text="Last Name")
table.column("last_name", width=75)

table.heading("major", text="Major")
table.column("major", width=150)

table.place(x=50, y=140)

get_connection()
create_tables()
sample_data_insertion()

def refresh_table():
    for i in table.get_children():
        table.delete(i)

    for i in view_students():
        table.insert("", tk.END, values=(i[0], i[1], i[2], i[3]))

root.mainloop()