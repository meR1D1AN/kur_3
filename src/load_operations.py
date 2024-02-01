import json


def load_operations_from_file(file_path):
    """
    Функция загрузки файла Json
    """
    with open(file_path) as file:
        data = json.load(file)
        return data
