import numpy

from src.provinces import Province
from src.population_number import PopulationNumber


class PlainTextReport(object):
    def __init__(self, dataset: list[Province]):
        self.report_lines = []
        self.provinces = dataset
        self.total_population = sum([x.population.value for x in self.provinces])
        self.column_headings = ["Province", "Population", "Capital City and Population"]
        self.cw = self.column_widths()

    def headings(self) -> str:
        return "{0:{3}}{1:>{4}}   {2:{5}}".format(*self.column_headings, *self.cw[0:3])

    def data_line(self, data: Province) -> str:
        return "".join([
            f"{data.name:<{self.cw[0]}}",
            f"{data.population.as_string():>{self.cw[1]}}   ",
            f"{data.capital.name:<{self.cw[2]}} ",
            f"{data.capital.population.as_string():>{self.cw[3]}}"
        ])

    def total_line(self):
        n = PopulationNumber(self.total_population).as_string()
        return f"TOTAL    {n:>{self.cw[1]}}"

    @staticmethod
    def numeric_field_width(n: int) -> int:
        d = int(numpy.floor(numpy.log10(n)))
        return d + d // 3 + 2

    def column_widths(self):
        col0 = max([len(x.name) for x in self.provinces])
        col0 = max(col0, len(self.column_headings[0])) + 1

        col1 = max(self.numeric_field_width(self.total_population),
                   len(self.column_headings[1]))

        col2 = max([len(x.capital.name) for x in self.provinces]) + 1

        col3 = self.numeric_field_width(max([x.capital.population.value for x in self.provinces]))

        return col0, col1, col2, col3

    def hline(self, char: str = '-', length: int = 0) -> str:
        """
        Return a 'horizontal line' composed, by default, of dashes.

        :param str char: A character to use instead of dash.
        Only the first character is used if a multi-character string is passed.
        :param int length: The length of the line.
        If omitted or given as a number less than or equal zero,
        line length is  based on the sum of calculated column widths.
        :return: The line
        :rtype: str
        :raises IndexError: If an empty string is passed as char.
        :raises TypeError: If length is not an integer
        """
        if length <= 0:
            length = sum(self.cw) + 6
        return char[0] * length

    def full_report(self):
        self.report_lines.append(self.hline())
        self.report_lines.append(self.headings())
        self.report_lines.append(self.hline())
        for item in self.provinces:
            self.report_lines.append(self.data_line(item))
        self.report_lines.append("")
        self.report_lines.append(self.total_line())
        self.report_lines.append(self.hline())
        return "\n".join(self.report_lines)

    def write_to_screen(self):
        print()
        print(self.full_report())
        print()

    def write_to_file(self):
        pass
