import pytest
import json


@pytest.mark.parametrize("file_path", ['../src/operations.json'])
def test_state_output(file_path):
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