import tkinter as tk
from tkinter import ttk, messagebox
from database import *

# login screen

current_role = None
current_user_id = None

def launch_login():
    login = tk.Tk()
    login.title("Student Management System — Login")
    login.geometry("400x280+560+300")
    login.resizable(False, False)

    ttk.Label(login, text="Student Management System", font=("Arial", 16, "bold")).pack(pady=(25, 5))
    ttk.Label(login, text="Select your role to continue", font=("Arial", 10)).pack(pady=(0, 20))

    role_var = tk.StringVar(value="Admin")

    role_frame = ttk.Frame(login)
    role_frame.pack()
    ttk.Radiobutton(role_frame, text="Admin",      variable=role_var, value="Admin").grid(row=0, column=0, padx=15)
    ttk.Radiobutton(role_frame, text="Student",    variable=role_var, value="Student").grid(row=0, column=1, padx=15)
    ttk.Radiobutton(role_frame, text="Instructor", variable=role_var, value="Instructor").grid(row=0, column=2, padx=15)

    id_frame = ttk.Frame(login)
    id_frame.pack(pady=15)
    id_label = ttk.Label(id_frame, text="ID (Student / Instructor):")
    id_label.grid(row=0, column=0, padx=(0, 8))
    id_entry = ttk.Entry(id_frame, width=12)
    id_entry.grid(row=0, column=1)

    error_label = ttk.Label(login, text="", foreground="red")
    error_label.pack()

    def on_login():
        global current_role, current_user_id
        role = role_var.get()
        uid = id_entry.get().strip()

        if role in ("Student", "Instructor"):
            if not uid:
                error_label.config(text=f"Please enter your {role} ID.")
                return
            if not uid.isdigit():
                error_label.config(text="ID must be a number.")
                return
            uid = int(uid)
            if role == "Student":
               rows = view_students()
               if not any(str(r[0]) == str(uid) for r in rows):
                    error_label.config(text="No student found with that ID.")
                    return
            else:
                rows = get_instructor_view(uid)
                if not rows:
                    error_label.config(text="No instructor found with that ID.")
                    return
            current_user_id = uid
        else:
            current_user_id = None

        current_role = role
        login.destroy()

    ttk.Button(login, text="Login", command=on_login, width=16).pack(pady=(5, 0))

    login.mainloop()

create_tables()
sample_data_insertion()
launch_login()

if current_role is None:
    import sys
    sys.exit()

# main window

if current_role in ("Student", "Instructor"):
    # read-only role view — separate simple window
    def launch_role_view():
        view = tk.Tk()
        view.resizable(True, True)

        if current_role == "Student":
            rows = get_student_view(current_user_id)

            student_rows = view_students()
            student = next((r for r in student_rows if str(r[0]) == str(current_user_id)), None)
            name = f"{student[1]} {student[2]}" if student else f"Student {current_user_id}"
            view.title(f"My Courses — {name}")
            view.geometry("900x500+200+150")

            ttk.Label(view, text=f"Welcome, {name}", font=("Arial", 16, "bold")).pack(pady=(15, 5))
            ttk.Label(view, text="Your enrolled courses and grades", font=("Arial", 10)).pack(pady=(0, 10))

            frame = ttk.Frame(view)
            frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

            scroll_y = ttk.Scrollbar(frame, orient="vertical")
            scroll_y.pack(side="right", fill="y")

            cols = ("course_id", "course_name", "credits", "instructor", "grade")
            table = ttk.Treeview(frame, columns=cols, show="headings", yscrollcommand=scroll_y.set)
            scroll_y.config(command=table.yview)

            col_cfg = [
                ("course_id",   "Course ID",   100),
                ("course_name", "Course Name", 280),
                ("credits",     "Credits",     80),
                ("instructor",  "Instructor",  220),
                ("grade",       "Grade",       80),
            ]
            for cid, text, w in col_cfg:
                table.heading(cid, text=text)
                table.column(cid, width=w, anchor="center")

            for r in rows:
                # r: student_id, student_name, course_id, course_name, credits, instructor_name, grade
                table.insert("", tk.END, values=(r[2], r[3], r[4], r[5] or "N/A", r[6]))

            table.pack(fill="both", expand=True)

        else:  # Instructor
            rows = get_instructor_view(current_user_id)
            name = rows[0][1] if rows else f"Instructor {current_user_id}"
            view.title(f"My Classes — {name}")
            view.geometry("1000x500+200+150")

            ttk.Label(view, text=f"Welcome, {name}", font=("Arial", 16, "bold")).pack(pady=(15, 5))
            ttk.Label(view, text="Your courses and enrolled students", font=("Arial", 10)).pack(pady=(0, 10))

            frame = ttk.Frame(view)
            frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

            scroll_y = ttk.Scrollbar(frame, orient="vertical")
            scroll_y.pack(side="right", fill="y")

            cols = ("course_id", "course_name", "student_id", "student_name", "major", "grade")
            table = ttk.Treeview(frame, columns=cols, show="headings", yscrollcommand=scroll_y.set)
            scroll_y.config(command=table.yview)

            col_cfg = [
                ("course_id",    "Course ID",    90),
                ("course_name",  "Course Name",  220),
                ("student_id",   "Student ID",   90),
                ("student_name", "Student Name", 180),
                ("major",        "Major",        170),
                ("grade",        "Grade",        80),
            ]
            for cid, text, w in col_cfg:
                table.heading(cid, text=text)
                table.column(cid, width=w, anchor="center")

            for r in rows:
                # r: instructor_id, instructor_name, course_id, course_name, student_id, student_name, major, grade
                table.insert("", tk.END, values=(r[2], r[3], r[4] or "—", r[5] or "—", r[6] or "—", r[7] or "—"))

            table.pack(fill="both", expand=True)

        view.mainloop()

    launch_role_view()
    import sys
    sys.exit()

root = tk.Tk()
root.title("Student Management System")
root.geometry("1300x700+200+100") 

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
students_form_frame = ttk.Frame(students_tab, height=145)
students_form_frame.pack(fill="x", side="top")
students_form_frame.pack_propagate(False)

students_table_frame = ttk.Frame(students_tab)
students_table_frame.pack(fill="both", expand=True, side="top")

students_table = ttk.Treeview(students_table_frame, columns=("student_id", "first_name", "last_name", "major"), show="headings")

students_table.heading("student_id", text="Student ID")
students_table.column("student_id", width=300, anchor="center")

students_table.heading("first_name", text="First Name")
students_table.column("first_name", width=300, anchor="center")

students_table.heading("last_name", text="Last Name")
students_table.column("last_name", width=300, anchor="center")

students_table.heading("major", text="Major")
students_table.column("major", width=300, anchor="center")

students_scroll_y = ttk.Scrollbar(students_table_frame, orient="vertical", command=students_table.yview)
students_table.configure(yscrollcommand=students_scroll_y.set)
students_scroll_y.pack(side="right", fill="y")
students_table.pack(fill="both", expand=True)

student_first_label = ttk.Label(students_form_frame, text="First Name:")
student_first_label.place(x=20, y=28)

student_first_entry = tk.StringVar()
student_first = ttk.Entry(students_form_frame, textvariable=student_first_entry, width=20)
student_first.place(x=100, y=25)

student_last_label = ttk.Label(students_form_frame, text="Last Name:")
student_last_label.place(x=270, y=28)

student_last_entry = tk.StringVar()
student_last = ttk.Entry(students_form_frame, textvariable=student_last_entry, width=20)
student_last.place(x=350, y=25)

student_id_label = ttk.Label(students_form_frame, text="Student ID:")
student_id_label.place(x=20, y=68)

student_id_entry = tk.StringVar()
student_id = ttk.Entry(students_form_frame, textvariable=student_id_entry, width=20)
student_id.place(x=100, y=65)

major_label = ttk.Label(students_form_frame, text="Major:")
major_label.place(x=285, y=68)

major_entry = tk.StringVar()
major = ttk.Entry(students_form_frame, textvariable=major_entry, width=20)
major.place(x=350, y=65)

def handle_add_student():
    sid = student_id_entry.get().strip()
    first = student_first_entry.get().strip()
    last = student_last_entry.get().strip()
    maj = major_entry.get().strip()

    if not sid or not first or not last or not maj:
        messagebox.showerror("Error", "All fields are required to add a student.")
        return
    if not sid.isdigit():
        messagebox.showerror("Error", "Student ID must be a number.")
        return

    try:
        add_student(sid, first, last, maj)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add student:\n{e}")
        return

    student_first_entry.set("")
    student_last_entry.set("")
    student_id_entry.set("")
    major_entry.set("")

    refresh_students_table()
    refresh_overview_table()

add_student_button = ttk.Button(students_form_frame, text="Add Student", command=handle_add_student)
add_student_button.place(x=20, y=110)

def handle_delete_student():
    sid = student_id_entry.get().strip()

    if not sid:
        messagebox.showerror("Error", "Student ID is required to delete a student.")
        return
    if not sid.isdigit():
        messagebox.showerror("Error", "Student ID must be a number.")
        return

    try:
        delete_student(sid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete student:\n{e}")
        return

    student_id_entry.set("")

    refresh_students_table()
    refresh_overview_table()

delete_student_button = ttk.Button(students_form_frame, text="Delete Student", command=handle_delete_student)
delete_student_button.place(x=145, y=110)

def handle_update_student():
    sid = student_id_entry.get().strip()
    first = student_first_entry.get().strip()
    last = student_last_entry.get().strip()
    maj = major_entry.get().strip()

    if not sid or not first or not last or not maj:
        messagebox.showerror("Error", "All fields are required to update a student.")
        return
    if not sid.isdigit():
        messagebox.showerror("Error", "Student ID must be a number.")
        return

    try:
        update_student(sid, first, last, maj)
    except Exception as e:
        messagebox.showerror("Error", f"Could not update student:\n{e}")
        return

    student_first_entry.set("")
    student_last_entry.set("")
    student_id_entry.set("")
    major_entry.set("")

    refresh_students_table()
    refresh_overview_table()

update_student_button = ttk.Button(students_form_frame, text="Update Student", command=handle_update_student)
update_student_button.place(x=280, y=110)

def on_student_select(event):
    selected = students_table.focus()
    if not selected:
        return
    values = students_table.item(selected, "values")
    student_id_entry.set(values[0])
    student_first_entry.set(values[1])
    student_last_entry.set(values[2])
    major_entry.set(values[3])

students_table.bind("<<TreeviewSelect>>", on_student_select)

# courses tab
courses_form_frame = ttk.Frame(courses_tab, height=145)
courses_form_frame.pack(fill="x", side="top")
courses_form_frame.pack_propagate(False)

courses_table_frame = ttk.Frame(courses_tab)
courses_table_frame.pack(fill="both", expand=True, side="top")

courses_table = ttk.Treeview(courses_table_frame, columns=("course_id", "department_id", "course_name", "credits"), show="headings")

courses_table.heading("course_id", text="Course ID")
courses_table.column("course_id", width=300, anchor="center")

courses_table.heading("department_id", text="Department ID")
courses_table.column("department_id", width=300, anchor="center")

courses_table.heading("course_name", text="Course Name")
courses_table.column("course_name", width=300, anchor="center")

courses_table.heading("credits", text="Credits")
courses_table.column("credits", width=300, anchor="center")

courses_scroll_y = ttk.Scrollbar(courses_table_frame, orient="vertical", command=courses_table.yview)
courses_table.configure(yscrollcommand=courses_scroll_y.set)
courses_scroll_y.pack(side="right", fill="y")
courses_table.pack(fill="both", expand=True)

course_id_label = ttk.Label(courses_form_frame, text="Course ID:")
course_id_label.place(x=20, y=28)

course_id_entry = tk.StringVar()
course_id = ttk.Entry(courses_form_frame, textvariable=course_id_entry, width=20)
course_id.place(x=100, y=25)

department_id_label = ttk.Label(courses_form_frame, text="Department ID:")
department_id_label.place(x=255, y=28)

department_id_entry = tk.StringVar()
department_id = ttk.Entry(courses_form_frame, textvariable=department_id_entry, width=20)
department_id.place(x=350, y=25)

course_name_label = ttk.Label(courses_form_frame, text="Course Name:")
course_name_label.place(x=20, y=68)

course_name_entry = tk.StringVar()
course_name = ttk.Entry(courses_form_frame, textvariable=course_name_entry, width=20)
course_name.place(x=100, y=65)

credits_label = ttk.Label(courses_form_frame, text="Credits:")
credits_label.place(x=285, y=68)

credits_entry = tk.StringVar()
credits = ttk.Entry(courses_form_frame, textvariable=credits_entry, width=20)
credits.place(x=350, y=65)

def handle_add_course():
    cid = course_id_entry.get().strip()
    did = department_id_entry.get().strip()
    cname = course_name_entry.get().strip()
    cred = credits_entry.get().strip()

    if not cid or not did or not cname or not cred:
        messagebox.showerror("Error", "All fields are required to add a course.")
        return
    if not cid.isdigit() or not did.isdigit() or not cred.isdigit():
        messagebox.showerror("Error", "Course ID, Department ID, and Credits must be numbers.")
        return

    try:
        add_course(cid, did, cname, cred)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add course:\n{e}")
        return

    course_id_entry.set("")
    department_id_entry.set("")
    course_name_entry.set("")
    credits_entry.set("")

    refresh_courses_table()
    refresh_overview_table()

add_course_button = ttk.Button(courses_form_frame, text="Add Course", command=handle_add_course)
add_course_button.place(x=20, y=110)

def handle_delete_course():
    cid = course_id_entry.get().strip()

    if not cid:
        messagebox.showerror("Error", "Course ID is required to delete a course.")
        return
    if not cid.isdigit():
        messagebox.showerror("Error", "Course ID must be a number.")
        return

    try:
        delete_course(cid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete course:\n{e}")
        return

    course_id_entry.set("")

    refresh_courses_table()
    refresh_overview_table()

delete_course_button = ttk.Button(courses_form_frame, text="Delete Course", command=handle_delete_course)
delete_course_button.place(x=140, y=110)

def handle_update_course():
    cid = course_id_entry.get().strip()
    did = department_id_entry.get().strip()
    cname = course_name_entry.get().strip()
    cred = credits_entry.get().strip()

    if not cid or not did or not cname or not cred:
        messagebox.showerror("Error", "All fields are required to update a course.")
        return
    if not cid.isdigit() or not did.isdigit() or not cred.isdigit():
        messagebox.showerror("Error", "Course ID, Department ID, and Credits must be numbers.")
        return

    try:
        update_course(cid, did, cname, cred)
    except Exception as e:
        messagebox.showerror("Error", f"Could not update course:\n{e}")
        return

    course_id_entry.set("")
    department_id_entry.set("")
    course_name_entry.set("")
    credits_entry.set("")

    refresh_courses_table()
    refresh_overview_table()

update_course_button = ttk.Button(courses_form_frame, text="Update Course", command=handle_update_course)
update_course_button.place(x=270, y=110)

def on_course_select(event):
    selected = courses_table.focus()
    if not selected:
        return
    values = courses_table.item(selected, "values")
    course_id_entry.set(values[0])
    department_id_entry.set(values[1])
    course_name_entry.set(values[2])
    credits_entry.set(values[3])

courses_table.bind("<<TreeviewSelect>>", on_course_select)

# instructors tab
instructors_form_frame = ttk.Frame(instructors_tab, height=145)
instructors_form_frame.pack(fill="x", side="top")
instructors_form_frame.pack_propagate(False)

instructors_table_frame = ttk.Frame(instructors_tab)
instructors_table_frame.pack(fill="both", expand=True, side="top")

instructors_table = ttk.Treeview(instructors_table_frame, columns=("instructor_id", "department_id", "first_name", "last_name"), show="headings")

instructors_table.heading("instructor_id", text="Instructor ID")
instructors_table.column("instructor_id", width=300, anchor="center")

instructors_table.heading("department_id", text="Department ID")
instructors_table.column("department_id", width=300, anchor="center")

instructors_table.heading("first_name", text="First Name")
instructors_table.column("first_name", width=300, anchor="center")

instructors_table.heading("last_name", text="Last Name")
instructors_table.column("last_name", width=300, anchor="center")

instructors_scroll_y = ttk.Scrollbar(instructors_table_frame, orient="vertical", command=instructors_table.yview)
instructors_table.configure(yscrollcommand=instructors_scroll_y.set)
instructors_scroll_y.pack(side="right", fill="y")
instructors_table.pack(fill="both", expand=True)

instructor_id_label = ttk.Label(instructors_form_frame, text="Instructor ID:")
instructor_id_label.place(x=20, y=28)

instructor_id_entry = tk.StringVar()
instructor_id = ttk.Entry(instructors_form_frame, textvariable=instructor_id_entry, width=20)
instructor_id.place(x=110, y=25)

instructor_department_id_label = ttk.Label(instructors_form_frame, text="Department ID:")
instructor_department_id_label.place(x=270, y=28)

instructor_department_id_entry = tk.StringVar()
instructor_department_id = ttk.Entry(instructors_form_frame, textvariable=instructor_department_id_entry, width=20)
instructor_department_id.place(x=370, y=25)

instructor_first_label = ttk.Label(instructors_form_frame, text="First Name:")
instructor_first_label.place(x=20, y=68)

instructor_first_entry = tk.StringVar()
instructor_first = ttk.Entry(instructors_form_frame, textvariable=instructor_first_entry, width=20)
instructor_first.place(x=110, y=65)

instructor_last_label = ttk.Label(instructors_form_frame, text="Last Name:")
instructor_last_label.place(x=270, y=68)

instructor_last_entry = tk.StringVar()
instructor_last = ttk.Entry(instructors_form_frame, textvariable=instructor_last_entry, width=20)
instructor_last.place(x=370, y=65)

def handle_add_instructor():
    iid = instructor_id_entry.get().strip()
    did = instructor_department_id_entry.get().strip()
    first = instructor_first_entry.get().strip()
    last = instructor_last_entry.get().strip()

    if not iid or not did or not first or not last:
        messagebox.showerror("Error", "All fields are required to add an instructor.")
        return
    if not iid.isdigit() or not did.isdigit():
        messagebox.showerror("Error", "Instructor ID and Department ID must be numbers.")
        return

    try:
        add_instructor(iid, did, first, last)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add instructor:\n{e}")
        return

    instructor_id_entry.set("")
    instructor_department_id_entry.set("")
    instructor_first_entry.set("")
    instructor_last_entry.set("")

    refresh_instructors_table()
    refresh_overview_table()

add_instructor_button = ttk.Button(instructors_form_frame, text="Add Instructor", command=handle_add_instructor)
add_instructor_button.place(x=20, y=110)

def handle_delete_instructor():
    iid = instructor_id_entry.get().strip()

    if not iid:
        messagebox.showerror("Error", "Instructor ID is required to delete an instructor.")
        return
    if not iid.isdigit():
        messagebox.showerror("Error", "Instructor ID must be a number.")
        return

    try:
        delete_instructor(iid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete instructor:\n{e}")
        return

    instructor_id_entry.set("")

    refresh_instructors_table()
    refresh_overview_table()

delete_instructor_button = ttk.Button(instructors_form_frame, text="Delete Instructor", command=handle_delete_instructor)
delete_instructor_button.place(x=150, y=110)

def handle_update_instructor():
    iid = instructor_id_entry.get().strip()
    did = instructor_department_id_entry.get().strip()
    first = instructor_first_entry.get().strip()
    last = instructor_last_entry.get().strip()

    if not iid or not did or not first or not last:
        messagebox.showerror("Error", "All fields are required to update an instructor.")
        return
    if not iid.isdigit() or not did.isdigit():
        messagebox.showerror("Error", "Instructor ID and Department ID must be numbers.")
        return

    try:
        update_instructor(iid, did, first, last)
    except Exception as e:
        messagebox.showerror("Error", f"Could not update instructor:\n{e}")
        return

    instructor_id_entry.set("")
    instructor_department_id_entry.set("")
    instructor_first_entry.set("")
    instructor_last_entry.set("")

    refresh_instructors_table()
    refresh_overview_table()

update_instructor_button = ttk.Button(instructors_form_frame, text="Update Instructor", command=handle_update_instructor)
update_instructor_button.place(x=290, y=110)

def on_instructor_select(event):
    selected = instructors_table.focus()
    if not selected:
        return
    values = instructors_table.item(selected, "values")
    instructor_id_entry.set(values[0])
    instructor_department_id_entry.set(values[1])
    instructor_first_entry.set(values[2])
    instructor_last_entry.set(values[3])

instructors_table.bind("<<TreeviewSelect>>", on_instructor_select)

# enrollments table
enrollments_form_frame = ttk.Frame(enrollments_tab, height=145)
enrollments_form_frame.pack(fill="x", side="top")
enrollments_form_frame.pack_propagate(False)

enrollments_table_frame = ttk.Frame(enrollments_tab)
enrollments_table_frame.pack(fill="both", expand=True, side="top")

enrollments_table = ttk.Treeview(
    enrollments_table_frame,
    columns=("enrollment_id", "course_id", "student_id", "grade"),
    show="headings"
)

enrollments_table.heading("enrollment_id", text="Enrollment ID")
enrollments_table.column("enrollment_id", width=300, anchor="center")

enrollments_table.heading("course_id", text="Course ID")
enrollments_table.column("course_id", width=300, anchor="center")

enrollments_table.heading("student_id", text="Student ID")
enrollments_table.column("student_id", width=300, anchor="center")

enrollments_table.heading("grade", text="Grade")
enrollments_table.column("grade", width=300, anchor="center")

enrollments_scroll_y = ttk.Scrollbar(enrollments_table_frame, orient="vertical", command=enrollments_table.yview)
enrollments_table.configure(yscrollcommand=enrollments_scroll_y.set)
enrollments_scroll_y.pack(side="right", fill="y")
enrollments_table.pack(fill="both", expand=True)

enrollment_id_label = ttk.Label(enrollments_form_frame, text="Enrollment ID:")
enrollment_id_label.place(x=20, y=28)

enrollment_id_entry = tk.StringVar()
enrollment_id = ttk.Entry(enrollments_form_frame, textvariable=enrollment_id_entry, width=20)
enrollment_id.place(x=110, y=25)

enrollment_course_id_label = ttk.Label(enrollments_form_frame, text="Course ID:")
enrollment_course_id_label.place(x=270, y=28)

enrollment_course_id_entry = tk.StringVar()
enrollment_course_id = ttk.Entry(enrollments_form_frame, textvariable=enrollment_course_id_entry, width=20)
enrollment_course_id.place(x=350, y=25)

enrollment_student_id_label = ttk.Label(enrollments_form_frame, text="Student ID:")
enrollment_student_id_label.place(x=20, y=68)

enrollment_student_id_entry = tk.StringVar()
enrollment_student_id = ttk.Entry(enrollments_form_frame, textvariable=enrollment_student_id_entry, width=20)
enrollment_student_id.place(x=110, y=65)

grade_label = ttk.Label(enrollments_form_frame, text="Grade:")
grade_label.place(x=285, y=68)

grade_entry = tk.StringVar()
grade = ttk.Entry(enrollments_form_frame, textvariable=grade_entry, width=20)
grade.place(x=350, y=65)

def handle_add_enrollment():
    eid = enrollment_id_entry.get().strip()
    cid = enrollment_course_id_entry.get().strip()
    sid = enrollment_student_id_entry.get().strip()
    g = grade_entry.get().strip()

    if not eid or not cid or not sid or not g:
        messagebox.showerror("Error", "All fields are required to add an enrollment.")
        return
    if not eid.isdigit() or not cid.isdigit() or not sid.isdigit():
        messagebox.showerror("Error", "Enrollment ID, Course ID, and Student ID must be numbers.")
        return

    try:
        add_enrollment(eid, cid, sid, g)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add enrollment:\n{e}")
        return

    enrollment_id_entry.set("")
    enrollment_course_id_entry.set("")
    enrollment_student_id_entry.set("")
    grade_entry.set("")

    refresh_enrollments_table()
    refresh_overview_table()

add_enrollment_button = ttk.Button(enrollments_form_frame, text="Add Enrollment", command=handle_add_enrollment)
add_enrollment_button.place(x=20, y=110)

def handle_delete_enrollment():
    eid = enrollment_id_entry.get().strip()

    if not eid:
        messagebox.showerror("Error", "Enrollment ID is required to delete an enrollment.")
        return
    if not eid.isdigit():
        messagebox.showerror("Error", "Enrollment ID must be a number.")
        return

    try:
        delete_enrollment(eid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete enrollment:\n{e}")
        return

    enrollment_id_entry.set("")

    refresh_enrollments_table()
    refresh_overview_table()

delete_enrollment_button = ttk.Button(enrollments_form_frame, text="Delete Enrollment", command=handle_delete_enrollment)
delete_enrollment_button.place(x=155, y=110)

def handle_update_enrollment():
    eid = enrollment_id_entry.get().strip()
    cid = enrollment_course_id_entry.get().strip()
    sid = enrollment_student_id_entry.get().strip()
    g = grade_entry.get().strip()

    if not eid or not cid or not sid or not g:
        messagebox.showerror("Error", "All fields are required to update an enrollment.")
        return
    if not eid.isdigit() or not cid.isdigit() or not sid.isdigit():
        messagebox.showerror("Error", "Enrollment ID, Course ID, and Student ID must be numbers.")
        return

    try:
        update_enrollment(eid, cid, sid, g)
    except Exception as e:
        messagebox.showerror("Error", f"Could not update enrollment:\n{e}")
        return

    enrollment_id_entry.set("")
    enrollment_course_id_entry.set("")
    enrollment_student_id_entry.set("")
    grade_entry.set("")

    refresh_enrollments_table()
    refresh_overview_table()

update_enrollment_button = ttk.Button(enrollments_form_frame, text="Update Enrollment", command=handle_update_enrollment)
update_enrollment_button.place(x=300, y=110)

def on_enrollment_select(event):
    selected = enrollments_table.focus()
    if not selected:
        return
    values = enrollments_table.item(selected, "values")
    enrollment_id_entry.set(values[0])
    enrollment_course_id_entry.set(values[1])
    enrollment_student_id_entry.set(values[2])
    grade_entry.set(values[3])

enrollments_table.bind("<<TreeviewSelect>>", on_enrollment_select)

# teaches tab
teaches_form_frame = ttk.Frame(teaches_tab, height=145)
teaches_form_frame.pack(fill="x", side="top")
teaches_form_frame.pack_propagate(False)

teaches_table_frame = ttk.Frame(teaches_tab)
teaches_table_frame.pack(fill="both", expand=True, side="top")

teaches_table = ttk.Treeview(
    teaches_table_frame,
    columns=("instructor_id", "course_id"),
    show="headings"
)

teaches_table.heading("instructor_id", text="Instructor ID")
teaches_table.column("instructor_id", width=600, anchor="center")

teaches_table.heading("course_id", text="Course ID")
teaches_table.column("course_id", width=600, anchor="center")

teaches_scroll_y = ttk.Scrollbar(teaches_table_frame, orient="vertical", command=teaches_table.yview)
teaches_table.configure(yscrollcommand=teaches_scroll_y.set)
teaches_scroll_y.pack(side="right", fill="y")
teaches_table.pack(fill="both", expand=True)

teaches_instructor_id_label = ttk.Label(teaches_form_frame, text="Instructor ID:")
teaches_instructor_id_label.place(x=20, y=48)

teaches_instructor_id_entry = tk.StringVar()
teaches_instructor_id = ttk.Entry(teaches_form_frame, textvariable=teaches_instructor_id_entry, width=20)
teaches_instructor_id.place(x=110, y=45)

teaches_course_id_label = ttk.Label(teaches_form_frame, text="Course ID:")
teaches_course_id_label.place(x=290, y=48)

teaches_course_id_entry = tk.StringVar()
teaches_course_id = ttk.Entry(teaches_form_frame, textvariable=teaches_course_id_entry, width=20)
teaches_course_id.place(x=370, y=45)

def handle_add_teaches():
    iid = teaches_instructor_id_entry.get().strip()
    cid = teaches_course_id_entry.get().strip()

    if not iid or not cid:
        messagebox.showerror("Error", "Both Instructor ID and Course ID are required.")
        return
    if not iid.isdigit() or not cid.isdigit():
        messagebox.showerror("Error", "Instructor ID and Course ID must be numbers.")
        return

    try:
        add_teaches(iid, cid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add teaches record:\n{e}")
        return

    teaches_instructor_id_entry.set("")
    teaches_course_id_entry.set("")

    refresh_teaches_table()
    refresh_overview_table()

add_teaches_button = ttk.Button(teaches_form_frame, text="Add Teaches", command=handle_add_teaches)
add_teaches_button.place(x=20, y=110)

def handle_delete_teaches():
    iid = teaches_instructor_id_entry.get().strip()
    cid = teaches_course_id_entry.get().strip()

    if not iid or not cid:
        messagebox.showerror("Error", "Both Instructor ID and Course ID are required to delete.")
        return
    if not iid.isdigit() or not cid.isdigit():
        messagebox.showerror("Error", "Instructor ID and Course ID must be numbers.")
        return

    try:
        delete_teaches(iid, cid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete teaches record:\n{e}")
        return

    teaches_instructor_id_entry.set("")
    teaches_course_id_entry.set("")

    refresh_teaches_table()
    refresh_overview_table()

delete_teaches_button = ttk.Button(teaches_form_frame, text="Delete Teaches", command=handle_delete_teaches)
delete_teaches_button.place(x=145, y=110)

def handle_update_teaches():
    iid = teaches_instructor_id_entry.get().strip()
    cid = teaches_course_id_entry.get().strip()

    if not iid or not cid:
        messagebox.showerror("Error", "Both Instructor ID and Course ID are required to update.")
        return
    if not iid.isdigit() or not cid.isdigit():
        messagebox.showerror("Error", "Instructor ID and Course ID must be numbers.")
        return

    try:
        update_teaches(iid, cid, iid, cid)
    except Exception as e:
        messagebox.showerror("Error", f"Could not update teaches record:\n{e}")
        return

    teaches_instructor_id_entry.set("")
    teaches_course_id_entry.set("")

    refresh_teaches_table()
    refresh_overview_table()

update_teaches_button = ttk.Button(teaches_form_frame, text="Update Teaches", command=handle_update_teaches)
update_teaches_button.place(x=280, y=110)

def on_teaches_select(event):
    selected = teaches_table.focus()
    if not selected:
        return
    values = teaches_table.item(selected, "values")
    teaches_instructor_id_entry.set(values[0])
    teaches_course_id_entry.set(values[1])

teaches_table.bind("<<TreeviewSelect>>", on_teaches_select)

# overview tab
overview_frame = ttk.Frame(overview_tab)
overview_frame.pack(fill="both", expand=True, padx=5, pady=5)

overview_scroll_y = ttk.Scrollbar(overview_frame, orient="vertical")
overview_scroll_y.pack(side="right", fill="y")

overview_scroll_x = ttk.Scrollbar(overview_frame, orient="horizontal")
overview_scroll_x.pack(side="bottom", fill="x")

overview_table = ttk.Treeview(
    overview_frame,
    columns=("student_id", "student_name", "course_id", "course_name", "instructor_id", "instructor_name", "major", "grade"),
    show="headings",
    height=25,
    yscrollcommand=overview_scroll_y.set,
    xscrollcommand=overview_scroll_x.set
)

overview_scroll_y.config(command=overview_table.yview)
overview_scroll_x.config(command=overview_table.xview)

overview_columns = [
    ("student_id", "Student ID", 90),
    ("student_name", "Student Name", 150),
    ("course_id", "Course ID", 90),
    ("course_name", "Course Name", 210),
    ("instructor_id", "Instructor ID", 100),
    ("instructor_name", "Instructor Name", 170),
    ("major", "Major", 160),
    ("grade", "Grade", 70)
]

for col, text, width in overview_columns:
    overview_table.heading(col, text=text)
    overview_table.column(col, width=width, anchor="center", minwidth=width)

overview_table.pack(fill="both", expand=True)

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

con = get_connection()
con.close()

refresh_students_table()
refresh_courses_table()
refresh_instructors_table()
refresh_enrollments_table()
refresh_teaches_table()
refresh_overview_table()

root.mainloop()