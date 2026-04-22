import tkinter as tk
from tkinter import messagebox

def save_data():
    # Get data from entry boxes
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    if name and age and course:
        # Display a success message with the info
        info = f"Name: {name}\nAge: {age}\nCourse: {course}"
        messagebox.showinfo("Student Saved", info)
    else:
        # Show error if a field is empty
        messagebox.showwarning("Input Error", "Please fill all fields!")

root = tk.Tk()
root.title("Student Info Form")
root.geometry("300x200")

# --- Row 0: Name ---
tk.Label(root, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# --- Row 1: Age ---
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# --- Row 2: Course ---
tk.Label(root, text="Course:").grid(row=2, column=0, padx=10, pady=5)
course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1)

# --- Row 3: Submit Button ---
submit_btn = tk.Button(root, text="Submit Info", command=save_data)
submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()