from src.provinces import ProvinceList, PopulationLaTexTable


class Application(object):
    def __init__(self):
        self.provinces = ProvinceList()

    def run(self):
        print()
        print(self.provinces.population_report())
        print()
        print(f"Interation count: {self.provinces.populations.iterations}")
        print()
        latex_table = PopulationLaTexTable(self.provinces)
        print(latex_table.latex_table())


if __name__ == '__main__':
    app = Application()
    app.run()
