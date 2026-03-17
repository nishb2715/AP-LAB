#Create a class Student with a display() method in python 
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Example usage:
student1 = Student("Alice", 20, "S12345")   
student1.display()
student2 = Student("Bob", 22, "S67890")
student2.display()
student3 = Student("Charlie", 19, "S54321")
student3.display()
