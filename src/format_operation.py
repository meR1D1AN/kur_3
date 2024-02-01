from load_operations import load_operations_from_file


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
    if description == "Открытие вклада":
        formatted_operation = (
            f"{formatted_date} {description}\n{masked_to_account}\n{amount} "
            f"{currency_name}\n")
    else:
        formatted_operation = (
            f"{formatted_date} {description}\n{masked_from_account} -> {masked_to_account}\n{amount} "
            f"{currency_name}\n")
    return formatted_operation
