from format_operation import format_operation
from datetime import datetime


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