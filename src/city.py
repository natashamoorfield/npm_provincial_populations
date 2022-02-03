from dataclasses import dataclass
from typing import Optional


@dataclass()
class City(object):
    """
    The City class, unsurprisingly, holds data about Calmarendian cities.
    """
    name: str
    population: Optional[int] = None

    def __post_init__(self):
        """
        Data validation
        Population can be None (to indicate missing information) but must otherwise be
        a non-negative integer; zero is treated as valid and indicates a city with no people.
        """
        if self.population is not None:
            if not isinstance(self.population, int):
                raise TypeError("Population must be None or a non-negative integer.")
            if self.population < 0:
                raise ValueError("Population must be None or a non-negative integer.")

    @property
    def population_string(self) -> str:
        if self.population is None:
            return "Unknown"
        return f"{self.population:,d}"
