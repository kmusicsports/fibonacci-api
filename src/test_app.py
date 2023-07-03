import pytest
from typing import Any, Dict, Optional

from app import handler, check_input

ERROR_MESSAGES = {
    "key": "KeyError: 'n'",
    "type": "TypeError: 'n' must be an integer number, not float",
    "any": "Error: There is no 'n' that must be an integer larger than 0",
    "value": "ValueError: 'n' must be larger than 0"
}
FIBONACCI_NUMBERS = [
    1, 1, 2, 3, 5,
    8, 13, 21, 34, 55,
    89, 144, 233, 377, 610,
    987, 1597, 2584, 4181, 6765
]


def test_handler_normal():
    """Test normal processing of handler method."""
    for i in range(1, 20):
        assert handler({"n": i}, None) == {"result": FIBONACCI_NUMBERS[i - 1]}


@pytest.mark.parametrize(("event", "expected"), [
    ({"not n": 10}, {"message": ERROR_MESSAGES["key"]}),
    ({"n": 0.5}, {"message": ERROR_MESSAGES["type"]}),
    ({"n": -1}, {"message": ERROR_MESSAGES["value"]}),
    ({"n": -0}, {"message": ERROR_MESSAGES["value"]}),
    ({"n": "0.5"}, {"message": ERROR_MESSAGES["any"]}),
    ({"n": "-1"}, {"message": ERROR_MESSAGES["any"]}),
    ({"n": "a"}, {"message": ERROR_MESSAGES["any"]})
])
def test_handler_error(event: Dict[str, Any],  expected: Dict[str, str]):
    """Test error processing of handler method."""
    assert handler(event, None) == expected


@pytest.mark.parametrize(("event", "expected"), [
    ({"not n": 10}, ERROR_MESSAGES["key"]),
    ({"n": 0.5}, ERROR_MESSAGES["type"]),
    ({"n": -1}, ERROR_MESSAGES["value"]),
    ({"n": -0}, ERROR_MESSAGES["value"]),
    ({"n": 1}, None),
    ({"n": "1"}, None),
    ({"n": "0.5"}, ERROR_MESSAGES["any"]),
    ({"n": "-1"}, ERROR_MESSAGES["any"]),
    ({"n": "a"}, ERROR_MESSAGES["any"])
])
def test_check_input(event: Dict[str, Any],  expected: Optional[str]):
    """Test normal and error processing of check_input method."""
    assert check_input(event) == expected
