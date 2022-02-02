import unittest
from src.city import City


class CityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vienna = City("Vienna")
        self.port_victoria = City("Port Victoria", 1200000)

    def test_initialization(self):
        self.assertEqual(self.vienna.name, "Vienna")
        self.assertIsNone(self.vienna.population)
        self.assertEqual(self.port_victoria.name, "Port Victoria")
        self.assertEqual(self.port_victoria.population, 1200000)

    def test_calculated_data(self):
        self.assertEqual(self.vienna.population_string, "Unknown")
        self.assertEqual(self.port_victoria.population_string, "1,200,000")

    def test_duff_population(self):
        self.assertRaises(ValueError, City, "Maryport", -10)
        self.assertRaises(TypeError, City, "Maryport", 10.5)


if __name__ == '__main__':
    unittest.main()
