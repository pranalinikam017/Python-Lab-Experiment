import json
import os

FILE_NAME = "student.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student(data):
    roll = input("Enter Roll Number: ")
    if roll in data:
        print("Student already exists!")
        return
    
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    data[roll] = {
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    
    save_data(data)
    print("Student added successfully!")

def view_students(data):
    if not data:
        print("No student records found.")
        return
    
    for roll, details in data.items():
        print(f"\nRoll No: {roll}")
        for key, value in details.items():
            print(f"{key}: {value}")

def main():
    data = load_data()
    
    while True:
        print("\n===== Student Biodata Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()