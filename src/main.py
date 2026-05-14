"""
Student Record System

This CLI-based application allows users to:
- Add students
- View students
- Search students
- Delete students

The program demonstrates:
- Lists
- Dictionaries
- Loops
- File handling
- Algorithms
- Error handling
"""

import os


# =========================
# GLOBAL LIST
# =========================
students = []
# =========================
# LOAD STUDENTS FROM FILE
# =========================
def load_students():
    """
    Loads student records from the text file.
    """

    if os.path.exists("data/students.txt"):

        file = open("data/students.txt", "r")

        for line in file:

            data = line.strip().split(",")

            if len(data) == 3:

                student = {
                    "id": data[0],
                    "name": data[1],
                    "course": data[2]
                }
                students.append(student)

        file.close()


# =========================
# SAVE STUDENT TO FILE
# =========================
def save_student(student):
    """
    Saves a single student record to the file.

    Args:
        student (dict): Student information.
    """

    file = open("data/students.txt", "a")

    file.write(
        student["id"] + "," +
        student["name"] + "," +
        student["course"] + "\n"
    )
    file.close()


# =========================
# REWRITE FILE
# =========================
def rewrite_file():
    """
    Rewrites the entire student file.
    """

    file = open("data/students.txt", "w")

    for student in students:

        file.write(
            student["id"] + "," +
            student["name"] + "," +
            student["course"] + "\n"
        )

    file.close()
# =========================
# ADD STUDENT
# =========================
def add_student():
    """
    Adds a new student record.
    """

    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)

    save_student(student)
    print("\nStudent added successfully!")


# =========================
# VIEW STUDENTS
# =========================
def view_students():
    """
    Displays all student records.
    """

    print("\n===== STUDENT LIST =====")

    if len(students) == 0:
        print("No students found.")

    else:

        for student in students:

            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])

# =========================
# SEARCH STUDENT
# =========================
def search_student():
    """
    Searches for a student using ID.
    """

    print("\n===== SEARCH STUDENT =====")

    search_id = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found!")
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])

            found = True
            break

    if found is False:
        print("\nStudent not found.")


# =========================
# DELETE STUDENT
# =========================
def delete_student():
    """
    Deletes a student record.
    """

    print("\n===== DELETE STUDENT =====")

    delete_id = input("Enter Student ID: ")

    found = False

    for student in students:
        if student["id"] == delete_id:

            students.remove(student)

            found = True
            break

    if found:

        rewrite_file()

        print("\nStudent deleted successfully!")

    else:
        print("\nStudent not found.")


# =========================
# DISPLAY MENU
# =========================
def display_menu():
    """
    Displays the main menu.
    """

    print("\n==============================")
    print(" STUDENT RECORD SYSTEM ")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


# =========================
# MAIN FUNCTION
# =========================
def main():
    """
    Main program loop.
    """

    load_students()

while True:

        display_menu()

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("\nProgram exited.")
            break

        else:
            print("\nInvalid choice. Try again.")

# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    main()
