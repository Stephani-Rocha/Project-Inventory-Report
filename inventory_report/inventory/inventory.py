from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
# import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, type_report):
        with open(path, encoding='utf-8') as file:

            if path.endswith(".csv"):
                data = csv.DictReader(file)
                data_list = list(data)
            elif path.endswith(".json"):
                data_list = json.load(file)
            # else:
            #     my_xml = file.read()
            #     my_dict = xmltodict.parse(my_xml)
            #     data_list = my_dict["dataset"]["record"]

        if type_report == "simples":
            simple_report = SimpleReport.generate(data_list)
            return simple_report
        if type_report == "completo":
            complete_report = CompleteReport.generate(data_list)
            return complete_report
