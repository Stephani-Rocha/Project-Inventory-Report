import json


class ImportDataJSON:
    @staticmethod
    def generate(path):
        with open(path, encoding='utf-8') as file:
            data_list = json.load(file)
        return data_list
