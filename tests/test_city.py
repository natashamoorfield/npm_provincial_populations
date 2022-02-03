import unittest
from src.city import City


class CityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vienna = City("Vienna")
        self.port_victoria = City("Port Victoria", 1200000)
        self.deserted_city = City("Tumbleweed", 0)

    def test_valid_initialization(self):
        self.assertEqual(self.vienna.name, "Vienna")
        self.assertIsNone(self.vienna.population.value)
        self.assertEqual(self.port_victoria.name, "Port Victoria")
        self.assertEqual(self.port_victoria.population.value, 1200000)
        self.assertEqual(self.deserted_city.population.value, 0)
        c17 = City("City 17", 10.75)
        self.assertEqual(c17.population.value, 11)

    def test_calculated_data(self):
        self.assertEqual(self.vienna.population.as_string(), "unknown")
        self.assertEqual(self.port_victoria.population.as_string(), "1,200,000")

    def test_duff_population(self):
        self.assertRaises(ValueError, City, "Maryport", -10)


if __name__ == '__main__':
    unittest.main()
