import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do combos like 'Santiago, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does adding a population number work?"""
        formatted_city = get_formatted_city('Santiago', 'Chile', 500000)
        self.assertEqual(formatted_city, 'Santiago, Chile, Population - 500000')

if __name__ == '__main__':
    unittest.main()