import pytest
import json

from src.main import mask_account_number


@pytest.mark.parametrize("file_path", ['../operations.json'])
def test_state_output(file_path):
    """
    Тест проверки состояния операции
    """
    with open(file_path) as file:
        data = json.load(file)
        for operation in data:
            state = operation.get('state')
            if state == "EXECUTED":
                assert display_state(state) == state
            elif state == "CANCELED":
                assert display_state(state) == ""


def display_state(state):
    if state == "EXECUTED":
        return state
    else:
        return ""


def test_mask_accout_number_account():
    """
    Тест проверки маскирования номера счета
    :return:
    """
    account_number = "Счет 123456789012"
    masked_number = mask_account_number(account_number)
    assert masked_number == "Счет **9012"


def test_mask_account_number_card():
    """
    Тест проверки маскирования номера карты
    """
    card_number = "Maestro 1308795367077170"
    masked_number = mask_account_number(card_number)
    assert masked_number == "Maestro 1308 79** **** 7170"
