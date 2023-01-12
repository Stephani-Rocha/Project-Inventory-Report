from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(file):
        report = super(CompleteReport, CompleteReport).generate(file)
        names_company = [company["nome_da_empresa"] for company in file]
        companys_and_products = Counter(names_company)
        report += "\nProdutos estocados por empresa:\n"
        for company, qtd_product in companys_and_products.items():
            report += f"- {company}: {qtd_product}\n"
        return report
