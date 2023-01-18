import xmltodict


class ImportDataXML:
    @staticmethod
    def generate(path):
        with open(path, encoding='utf-8') as file:
            my_xml = file.read()
            my_dict = xmltodict.parse(my_xml)
            data_list = my_dict["dataset"]["record"]
        return data_list
