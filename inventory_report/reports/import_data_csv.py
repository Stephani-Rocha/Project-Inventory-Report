import csv


class ImportDataCSV:
    @staticmethod
    def generate(path):
        with open(path, encoding='utf-8') as file:
            data = csv.DictReader(file)
            data_list = list(data)
        return data_list
