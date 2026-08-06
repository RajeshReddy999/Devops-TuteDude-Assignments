student_grades = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Display All Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print("Student added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nStudent Grades")
        for name, grade in student_grades.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")


# E:\tutedude\devops\python-learning ❯ python .\student_grade_manage.py                  18:20:43 

# 1. Add Student
# 2. Update Student Grade
# 3. Display All Grades
# 4. Exit
# Enter your choice: 1
# Enter student name: Rajesh
# Enter grade: 90
# Student added successfully.
                                                                                                
# 1. Add Student
# 2. Update Student Grade
# 3. Display All Grades
# 4. Exit
# Enter your choice: 3

# Student Grades
# Rajesh : 90

# 1. Add Student
# 2. Update Student Grade
# 3. Display All Grades
# 4. Exit
# Enter your choice: 4
# Program ended.
# E:\tutedude\devops\python-learning ❯           
