"""A class for user information."""
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