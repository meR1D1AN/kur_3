import json
from datetime import datetime


def load_operations_from_file(file_path):
    """
    Функция загрузки файла Json
    """
    with open(file_path) as file:
        data = json.load(file)
        return data


# Путь к файлу JSON
file_path = 'operations.json'
# Загрузка данных операций из файла operations.json
operations_data = load_operations_from_file(file_path)


def format_operation(operation):
    """
    Функция формирования данных по задаче
    """
    formatted_date = operation['date'].strftime('%d.%m.%Y')
    description = operation['description']
    from_account = operation.get('from', 'Unknown')
    to_account = operation.get('to', 'Unknown')
    operation_amount = operation['operationAmount']
    amount = operation_amount['amount']
    currency_name = operation_amount['currency']['name']
    masked_from_account = mask_account_number(from_account)  # Замена номера счета
    masked_to_account = mask_account_number(to_account)  # Замена номера счета
    if description == 'Открытие вклада':
        formatted_operation = (
            f"{formatted_date} {description}\n{masked_to_account}\n{amount} "
            f"{currency_name}\n")
    else:
        formatted_operation = (
            f"{formatted_date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} "
            f"{currency_name}\n")
    return formatted_operation


def display_last_5_operations(operations_data):
    """
    Функция вывода отсортированных последних 5 операций по дате, по убыванию
    """
    formatted_operations = []
    # Преобразуем даты в формат datetime для сортировки
    for operation in operations_data:
        if 'date' in operation:
            operation['date'] = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
    # Сортируем операции по дате в убывающем порядке
    sorted_operations = sorted(operations_data, key=lambda x: x.get('date', datetime.min), reverse=True)
    # Получаем последние 5 операций
    last_5_operations = sorted_operations[:5]
    # Форматируем и добавляем операции в список отображения
    for operation in last_5_operations:
        formatted_operation = format_operation(operation)
        formatted_operations.append(formatted_operation)
    display_string = '\n'.join(formatted_operations)  # Объединяем отформатированные операции разделителем
    return display_string


def mask_account_number(account_number):
    """
    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом)
    Номер счета замаскирован и не отображается целиком в формате  **XXXX
    (видны только последние 4 цифры номера счета).
    """
    if "Счет" in account_number:
        return "Счет **" + account_number[-4:]
    else:
        # найти первую цифру
        first_digit_index = next((i for i, c in enumerate(account_number) if c.isdigit()), None)
        if first_digit_index is not None:
            # Если найдена первая цифра, сформировать маскированный номер
            prefix = account_number[:first_digit_index]
            number_chunk = account_number[first_digit_index:]
            # Форматировать номер
            masked_number = f"{prefix}{number_chunk[:4]} {number_chunk[4:6]}** **** {number_chunk[-4:]}"
            return masked_number
        else:
            # Вернуть исходную строку, если неизвестный формат
            return account_number


# Вывод последних 5 операций
formatted_operations = display_last_5_operations(operations_data)
print(formatted_operations)
