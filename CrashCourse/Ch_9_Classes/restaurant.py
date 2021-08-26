"""A class that can be used to represent a restaurant"""

class Restaurant:

    """Simple attempt to describe a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display basic information about the restaurant"""
        print(f"This restaurant is called {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, patron_count):
        """Display a message of how many people have been served."""
        self.number_served = patron_count
        print(f"{self.restaurant_name} has served {self.number_served} people.")

    def increment_number_served(self, patrons):
        """Increment the count of people served with the given amount."""
        self.number_served += patrons
