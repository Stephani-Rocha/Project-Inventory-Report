from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.import_data_csv import ImportDataCSV
from inventory_report.reports.import_data_json import ImportDataJSON
from inventory_report.reports.import_data_xml import ImportDataXML


class Inventory:
    @staticmethod
    def import_data(path, type_report):
        if path.endswith(".csv"):
            data_list = ImportDataCSV.generate(path)
        elif path.endswith(".json"):
            data_list = ImportDataJSON.generate(path)
        else:
            data_list = ImportDataXML.generate(path)

        if type_report == "simples":
            simple_report = SimpleReport.generate(data_list)
            return simple_report
        if type_report == "completo":
            complete_report = CompleteReport.generate(data_list)
            return complete_report
            # teste: comentei aqui
