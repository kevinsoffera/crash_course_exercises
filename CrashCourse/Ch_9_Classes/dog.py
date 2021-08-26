# Capitalize classes in python

class Dog:
    """A simple attempt to model a dog."""

# A function that is part of a class is known as a method

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age
# Variables accessible through instances like above are known as attributes.

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

