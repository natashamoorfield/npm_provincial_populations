from enum import Enum
from typing import Union


class ThousandsSeparator(Enum):
    COMMA = ','
    SPACE = ' '
    DOT = '.'
    LATEX_NB_HALF_SPACE = '\\,'
    UNDERSCORE = "_"


class PopulationNumber(object):
    """Numbers representing population figures"""
    def __init__(self, value: Union[int, float] = None):
        self.value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: Union[int, float]):
        """
        Validate input values.
        'None' is accepted as representing 'value unknown'.
        Anything that is not a real number is invalid.
        Any value less than zero is invalid.
        All values are rounded to the nearest whole number.
        """
        if new_value is not None:
            error_message = f"Population must be None or a real, non-negative number, not '{new_value}'."
            if not isinstance(new_value, (int, float)):
                raise TypeError(error_message)
            if new_value < 0:
                raise ValueError(error_message)
            new_value = round(new_value)
        self._value = new_value

    def as_string(self, sep: ThousandsSeparator = ThousandsSeparator.COMMA, missing: str = 'unknown') -> str:
        """
        Return a thousands-separated string representation of the population value.
        :param sep: The typographical thousands-separator; the default is COMMA.
        :param missing: The string to return is the value is None. Default is 'unknown'.
        :return: Value as a string.
        """
        if self.value is None:
            return missing
        s = f"{self.value:,d}"
        return s.replace(',', sep.value)
