#Implement multilevel inheritance.
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Puppy(Dog):
    def speak(self):
        return "Puppy yaps"
# Example usage:
puppy = Puppy()
print(puppy.speak())  # Output: Puppy yaps

