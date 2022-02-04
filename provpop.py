from src.provinces import ProvincialDataset
from src.plain_text_report import PlainTextReport


class Application(object):
    def __init__(self):
        # self.provinces = ProvinceList()
        self.provincial_dataset = ProvincialDataset()

    def run(self):
        report = PlainTextReport(self.provincial_dataset.provinces_sorted_by("population", rev=True))
        report.write_to_screen()
        report.write_to_file()


if __name__ == '__main__':
    app = Application()
    app.run()
