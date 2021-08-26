import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee instance for use in all test methods."""
        self.new_employee = Employee('Kevin', 'Soffera', 42600)

    def test_give_default_raise(self):
        """Raises the employees salary by the default $5000."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 47600)

    def test_give_custom_raise(self):
        """Raises the employee's salary by a custom amount, $10000."""
        self.new_employee.give_raise(3000)
        self.assertEqual(self.new_employee.salary, 45600)

if __name__ == '__main__':
    unittest.main()
