#Write a Python program to create a file and write student details into it.
student_details = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"}
]

with open("student_details.txt", "w") as file:
    for student in student_details:
        file.write(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\n")