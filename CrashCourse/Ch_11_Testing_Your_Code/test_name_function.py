import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        # Assert methods verify that a result you received matches the result 
        #  you expected to receive.
        # This line says "Compare the value in formatted_name to the string
        #  'Janis Joplin'. If they are equal as expected, fine. But if they
        #  don't match, let me know!"

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

if __name__ == '__main__':
    unittest.main()