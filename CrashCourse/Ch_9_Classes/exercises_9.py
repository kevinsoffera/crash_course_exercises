# 9.1 Restaurant
# class Restaurant:

#     """Simple attempt to describe a restaurant"""

#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize restaurant name and cuisine"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Display basic information about the restaurant"""
#         print(f"This restaurant is called {self.restaurant_name}.")
#         print(f"The restaurant serves {self.cuisine_type} food.")

#     def open_restaurant(self):
#         """Display a message that the restaurant is open"""
#         print(f"{self.restaurant_name} is open.")

#     def set_number_served(self, patron_count):
#         """Display a message of how many people have been served."""
#         self.number_served = patron_count
#         print(f"{self.restaurant_name} has served {self.number_served} people.")

#     def increment_number_served(self, patrons):
#         """Increment the count of people served with the given amount."""
#         self.number_served += patrons


# my_restaurant = Restaurant("Fuhgeddaboutit", "Italian")

# print(f"My restaurant is called {my_restaurant.restaurant_name}.")
# print(f"My restaurant serves {my_restaurant.cuisine_type} food.")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# 9.2 Three Restaurants
# second_restaurant = Restaurant("Steel Plates", 'Crunchy')
# third_restaurant = Restaurant('Totem Bar', 'Elemental')

# second_restaurant.describe_restaurant()
# third_restaurant.describe_restaurant()

# 9.3 Users
class User:
    """Summarize user information"""

    def __init__(self, first_name, last_name, location, ele_type):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.ele_type = ele_type
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user"""
        print(f"{self.first_name.title()} {self.last_name.title()} is "
            f"from {self.location.title()} and is a {self.ele_type} type.")

    def greet_user(self):
        """Greets the user"""
        print(f"Hello {self.first_name.title()} from {self.location.title()}!")

    def increment_login_attempts(self):
        """Add the amount of logins to login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Sets login attempts to 0"""
        self.login_attempts = 0

# user_0 = User('kevin', 'soffera', 'collegeville', 'fire')
# user_1 = User('kormax', 'kafo', 'kormulite', 'kormo')
# user_2 = User('retvew', 'trypola', 'pompeii', 'normal')

# user_0.describe_user()
# user_0.greet_user()

# user_1.describe_user()
# user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

# 9.4 Number Served
# restaurant = Restaurant("Wall", "Stone")
# print(restaurant.number_served)
# restaurant.number_served = 64
# print(restaurant.number_served)
# restaurant.set_number_served(42)
# restaurant.increment_number_served(6)
# print(restaurant.number_served)

# 9.5 Login Attempts
#  See methods related to login attempts in class User in 9.3
# user_0.increment_login_attempts()
# user_0.increment_login_attempts()
# print(user_0.login_attempts)
# user_0.reset_login_attempts()
# print(user_0.login_attempts)

# 9.6 Ice Cream Stand
# class IceCreamStand(Restaurant):
#     """Simple attempt to represent an ice cream stand's menu."""

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['vanilla', 'chocolate', 'raspberry']
    

#     def display_flavors(self):
#         """Print a message that displays the ice cream flavors available."""
#         print("We offer the flavors: ")
#         for flavor in self.flavors:
#             print(flavor)

# my_icecreamstand = IceCreamStand("Mobius' Cream", "Ice Cream")
# my_icecreamstand.display_flavors()

# 9.7 Admin and 9.8 Privileges
class Admin(User):
    """Summarize information about an administrator."""

    def __init__(self, first_name, last_name, location, ele_type):
        super().__init__(first_name, last_name, location, ele_type)
        self.privileges = Privileges()

    
# my_admin = Admin('kevin', 'soffera', 'collegeville', 'fire')
# my_admin.show_privileges()

class Privileges:
    def __init__(self):
        """Simple summary of admin privileges."""
        self.privileges = ['can add post', "can delete post", "can ban user",
                           'can warp space-time']

    def show_privileges(self):
        """Display a message about the privileges of an admin"""
        print(f"The Admin can: ")
        for privilege in self.privileges:
            print(privilege)

# my_new_admin = Admin('yortie', 'trevalex', 'new york', 'space')
# my_new_admin.privileges.show_privileges()

# 9.9 Battery Upgrade - see electric_car.py

# 9.10 Imported Restaurant - see restaurant.py (module) and my_restaurant.py
# 9.11 Imported Admin - see admin.py (module) and my_admin.py
# 9.12 Multiple Modules - see admin.py, user.py, (modules) and my_admin.py

# 9.13 Dice
from random import randint
class Die:
    """Simple dice roll"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"{self.sides}-sided die roll: {randint(1,self.sides)}")

my_die = Die()
d_10 = Die(10)
d_20 = Die(20)
# d_20.roll_die()

# 9.14 Lottery
from random import choice
lottery = [9, 4, 6, 8, 3, 22, 43, 56, 87, 19, 'K', 'Z', 'N', 'O', 'E']
winning_ticket = [choice(lottery), choice(lottery), choice(lottery), 
                    choice(lottery)]
# print(f"If your ticket matches {winning_ticket}, then you win!")

# 9.15 Lottery Analysis
my_ticket = [9, 'K', '3', 22]
pulls = 0
# while my_ticket != winning_ticket:
#     print(pulls)
#     pulls += 1
#     if my_ticket == winning_ticket:
#         print(f"Total number of tries: {pulls}.")
#         break

# 9.16 Python Module of the Week = https://pymotw.com/
