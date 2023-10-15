import json


def sort_and_filter_json(filename):
    """ФИЛЬТРАЦИЯ ОПЕРАЦИЙ КОТОРЫЕ ПРОШЛИ УСПЕШНО(EXECUTED)"""
    # Загрузка JSON-файла
    with open(filename, 'r') as file:
        data = json.load(file)

    # Фильтрация значений
    filtered_data = [item for item in data if item.get("state") == "EXECUTED"]

    # Сохранение отфильтрованного JSON-файла
    with open(filename, 'w') as file:
        json.dump(filtered_data, file, indent=4)
