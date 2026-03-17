#Demonstrate method overriding.
class Parent:
    def show(self):
        print("This is the Parent class method.")
class Child(Parent):
    def show(self):
        print("This is the Child class method, overriding Parent class method.")
# Example usage:
child_instance = Child()
child_instance.show()  
