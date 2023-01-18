from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @staticmethod
    def import_data(path, type_report):
        with open(path, encoding='utf-8') as file:
            if path.endswith(".csv"):
                data = csv.DictReader(file)
                data_list = list(data)
            if path.endswith(".json"):
                data_list = json.load(file)

        if type_report == "simples":
            simple_report = SimpleReport.generate(data_list)
            return simple_report
        if type_report == "completo":
            complete_report = CompleteReport.generate(data_list)
            return complete_report
