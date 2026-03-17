#Implement operator overloading for + (add marks of two students).
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __add__(self, other):
        if isinstance(other, Student):
            return self.marks + other.marks
        return NotImplemented
# Example usage:
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)
total_marks = student1 + student2
print(f"Total Marks of {student1.name} and {student2.name}: {total_marks}")
