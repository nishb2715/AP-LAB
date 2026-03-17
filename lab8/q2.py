#Use a constructor to initialize object data.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
# Example usage:
car1 = Car("Ford", "Mustang", 2020)
car1.display_info()
car2 = Car("Honda", "Civic", 2019)
car2.display_info()
