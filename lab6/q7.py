#Store student records in a CSV file.
import csv
def store_student_records(students, csv_file_path):
    try:
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Age', 'Grade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({'Name': student['name'], 'Age': student['age'], 'Grade': student['grade']})
    except Exception as e:
        print(f"An error occurred while writing to the CSV file: {e}")
#usage:
students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 22, 'grade': 'B'},
    {'name': 'Charlie', 'age': 19, 'grade': 'C'}
]
csv_file_path = "C:\\Users\\NISHTHA\\Desktop\\student_records.csv" 
store_student_records(students, csv_file_path)
