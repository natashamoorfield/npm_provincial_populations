from enum import Enum
from typing import Union


class ThousandsSeparator(Enum):
    COMMA = ','
    SPACE = ' '
    DOT = '.'
    LATEX_NB_HALF_SPACE = '\\,'
    UNDERSCORE = "_"


class PopulationNumber(object):

    def __init__(self, value: Union[int, float] = None):
        self.value = value

    @property
    def value(self) -> int:
        return self._population

    @value.setter
    def value(self, value: int):
        """
        Validate input values.
        'None' is accepted as representing 'value unknown'.
        Anything that is not a real number is invalid.
        Any value less than zero is invalid.
        All values are rounded to the nearest whole number.
        """
        if value is not None:
            error_message = "Population must be None or a real, non-negative, numerical value."
            if not isinstance(value, (int, float)):
                raise TypeError(error_message)
            if value < 0:
                raise ValueError(error_message)
            value = round(value)
        self._population = value

    def as_string(self, sep: ThousandsSeparator = ThousandsSeparator.COMMA, missing: str = 'unknown'):
        if self.value is None:
            return missing
        s = f"{self.value:,d}"
        return s.replace(',', sep.value)
