class Employee:
    """Define basic info about an employee"""

    def __init__(self, first, last, salary):
        """Name and salary information"""
        self.first = first
        self.last = last
        self.salary = salary


    def give_raise(self, salary_raise = 5000):
        """Adds to the employee's salary, defaulted at $5000"""
        self.salary = self.salary + salary_raise
        