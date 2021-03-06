import operator
import numpy
from src.numbers import PopulationList


class Province(object):
    def __init__(self, name: str, capital: str, population: int):
        self.name = name
        self.capital = capital
        self.population = population

    def __repr__(self) -> tuple:
        return self.name, self.capital, self.population


class ProvinceList(object):
    TOTAL = "TOTAL"
    EMPTY_STRING = ""

    def __init__(self):
        """
        Set up a List of Province objects which includes details of name, capital city and population.
        """
        # The six provinces listed in ascending order of long-term average population.
        # the actual population order may vary from time to time, depending on cyclic and random fluctuations.
        self.province_names = ["Mercia", "Avon", "Bohemia", "Wessex", "Victoria", "Eden"]
        self.max_name_length = max([len(x) for x in self.province_names])
        self.capital_cities = ["Maryport", "Willowbridge", "Prague", "Westbury", "Port Victoria", "Vienna"]
        self.max_city_length = max(len(x) for x in self.capital_cities)
        self.headings = ("Province", "Capital City", "Population")

        # The generated population numbers.
        self.populations = PopulationList()

        self.provinces = [Province(*p) for p in
                          zip(self.province_names, self.capital_cities, self.populations.populations)]

    def provinces_sorted_by(self, sort_key: str, rev: bool = False) -> list[Province]:
        """
        Return a new list of provinces sorted on the attribute specified by sort_key, in reverse if rev is set to True.
        """
        return sorted(self.provinces, key=operator.attrgetter(sort_key), reverse=rev)

    def name_field_length(self) -> int:
        """
        Return the amount of space needed for the province names in the output table.
        """
        return max(self.max_name_length, len(self.headings[0])) + 2

    def capital_field_length(self) -> int:
        """
        Return the amount of space needed for the provinces' capital cities in the output table.
        """
        return max(self.max_city_length, len(self.headings[1])) + 2

    def population_field_length(self) -> int:
        """
        Return the amount of space needed for the provinces' populations in the output table.
        Taking the floor of the log, base 10, of the largest population figure (that is, the grand total), will give us
        the number of digits (less one) to make space for. Dividing this by three will tell us how many commas to allow
        for.
        """
        d = int(numpy.floor(numpy.log10(self.populations.total_population)))
        return max(d + d // 3 + 2, len(self.headings[2]))

    def population_report(self) -> str:
        f = (self.name_field_length(), self.capital_field_length(), self.population_field_length())
        out_string = f"{self.headings[0]:<{f[0]}}{self.headings[1]:<{f[1]}}{self.headings[2]:>{f[2]}}\n"
        out_string += "-" * sum(f) + "\n"
        for province in self.provinces_sorted_by('population', rev=True):
            out_string += f"{province.name:<{f[0]}}{province.capital:<{f[1]}}{province.population:>{f[2]},d}\n"
        out_string += \
            "\n" + f"{self.TOTAL:<{f[0]}}{self.EMPTY_STRING:<{f[1]}}{self.populations.total_population:>{f[2]},d}"
        return out_string


class PopulationLaTexTable(object):
    """
    A class to generate code needed to render the population data in tabular form for a LaTex document.
    """
    def __init__(self, provinces: ProvinceList):
        self.provinces = provinces
        self.province_data = provinces.provinces_sorted_by('population', rev=True)

    def latex_table(self) -> str:
        """
        Return a string containing the LaTex code that will render the population data in tabular form.
        """
        out_string = "\\begin{table}\n"
        out_string += "\\centering\n"
        out_string += "\\caption{Population Figures for the Western Provinces} \\vspace{1ex}\n"
        out_string += "\\label{tab:population}\n"
        out_string += "\\begin{tabular}{|l|l|r|}\n"
        out_string += "\\hline\n"
        out_string += self.headings()
        out_string += "\\hline\n"
        for item in self.province_data:
            out_string += self.data_line(item)
        out_string += self.total_line()
        out_string += "\\hline\n"
        out_string += "\\end{tabular}\n"
        out_string += "\\end{table}"
        return out_string

    def headings(self) -> str:
        """
        Return a string containing the column headings.
        """
        out_string = " & ".join(["\\textbf{" + item + "}" for item in self.provinces.headings])
        return out_string + "\\\\[1pt]\n"

    @staticmethod
    def data_line(province: Province) -> str:
        """
        Return a string that will render an individual data row in the table.
        :param: province: A Province object containing the required data for the table row.
        """
        out_string = province.name + " & "
        out_string += province.capital + " & "
        out_string += f"{province.population:,d}"
        return out_string + "\\\\\n"

    def total_line(self) -> str:
        """
        Return a string that will render the final grand-total row of the table.
        """
        out_string = "&&\\\\\n"
        out_string += F"TOTAL && {self.provinces.populations.total_population:,d}\\\\\n"
        return out_string
