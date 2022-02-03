import unittest

from src.population_number import PopulationNumber, ThousandsSeparator


class PopulationNumberTest(unittest.TestCase):
    def test_init(self):
        p_none = PopulationNumber()
        self.assertIsNone(p_none.value, None)
        p_zero = PopulationNumber(0)
        self.assertEqual(p_zero.value, 0)
        p_standard = PopulationNumber(1234567)
        self.assertEqual(p_standard.value, 1234567)
        p_real = PopulationNumber(10.55)
        # Positive real numbers are rounded to the nearest integer value.
        self.assertIsInstance(p_real.value, int)
        self.assertEqual(p_real.value, 11)

    def test_duff_input(self):
        # It might be interesting to speculate what it means for a city to have a negative population or a complex one,
        # but we regard them as invalid nevertheless.
        self.assertRaises(ValueError, PopulationNumber, -10)
        self.assertRaises(TypeError, PopulationNumber, 10 + 4j)
        # Although real values x: -0.5 <= x < 0 will round to zero (valid)
        # they are treated as invalid because they are less than zero.
        self.assertRaises(ValueError, PopulationNumber, -0.4)
        # String input is treated as invalid even if it could be parsed into a valid number.
        self.assertRaises(TypeError, PopulationNumber, "One Million")

    def test_changes(self):
        p = PopulationNumber(100000)
        self.assertEqual(p.value, 100000)
        p.value = 250000
        self.assertEqual(p.value, 250000)
        p.value = None
        self.assertIsNone(p.value)

    def test_duff_changes(self):
        p = PopulationNumber(100000)
        with self.assertRaises(ValueError):
            p.value = -10

    def test_as_string(self):
        p = PopulationNumber(1234567)
        self.assertEqual(p.as_string(), "1,234,567")
        self.assertEqual(p.as_string(sep=ThousandsSeparator.DOT), "1.234.567")
        self.assertEqual(p.as_string(sep=ThousandsSeparator.LATEX_NB_HALF_SPACE), "1\\,234\\,567")
        n = PopulationNumber()
        self.assertEqual(n.as_string(), "unknown")
        self.assertEqual(n.as_string(missing="tba"), "tba")
        self.assertEqual(n.as_string(sep=ThousandsSeparator.SPACE, missing="tba"), "tba")


if __name__ == '__main__':
    unittest.main()
