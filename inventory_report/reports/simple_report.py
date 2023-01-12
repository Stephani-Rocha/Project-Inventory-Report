from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(file):
        manufacturing_dates = [item["data_de_fabricacao"] for item in file]
        earliest_manufacturing_date = sorted(manufacturing_dates)[0]

        expiration_dates = [date["data_de_validade"] for date in file]
        closest_expiration_dates = sorted(expiration_dates)[0]

        names_company = [company["nome_da_empresa"] for company in file]
        company_plus_product = Counter(names_company).most_common(1)[0][0]

        return (
            "Data de fabricação mais antiga: "
            f"{earliest_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_dates}\n"
            f"Empresa com mais produtos: {company_plus_product}"
        )
