#Implement single inheritance.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
# Example usage:
dog = Dog()
print(dog.speak())  # Output: Dog barks