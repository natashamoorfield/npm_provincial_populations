from typing import Union
from src.population_number import PopulationNumber


class City(object):
    """
    The City class, unsurprisingly, holds data about Calmarendian cities.
    """
    def __init__(self, name: str, population: Union[int, float] = None):
        """
        Object initialization
        :param name:
        :param population: If omitted, it is assumed the population figure is unknown, not zero.
        """
        self.name = name
        self.population = PopulationNumber(population)
