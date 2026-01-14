#Q3.Write a program to copy contents from one file to another.
with open("student_details.txt", "r") as source_file:
    with open("copied_student_details.txt", "w") as dest_file:
        for line in source_file:
            dest_file.write(line)