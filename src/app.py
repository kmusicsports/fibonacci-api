from typing import Any, Dict, Optional, Union
import sympy


def handler(event: Dict[str, Any], context) -> Dict[str, Union[str, int]]:
    """Process events.

    Args:
        event (Dict[str, Any]): JSON that contains data
            for Lambda function to process
        context (_type_): object that provide methods and properties
            that provide information about the invocation, function,
            and runtime environment

    Returns:
        Dict[str, Union[str, int]]: JSON response
    """
    message = check_input(event)

    if message:
        return {"message": message}

    result = int(sympy.fibonacci(event["n"]))  # The nth fibonacci number
    return {"result": result}


def check_input(event: Dict[str, Any]) -> Optional[str]:
    """Check if the input value is expected.

    Args:
        event (Dict[str, Any]): JSON that contains data
            for Lambda function to process

    Returns:
        Optional[str]: If there is an error, a string message, otherwise, None
    """
    if "n" not in event:
        return "KeyError: 'n'"

    n = event["n"]

    if isinstance(n, str):
        if not str.isdigit(n):
            return "Error: There is no 'n' "\
                "that must be an integer larger than 0"
        n = int(n)

    if not isinstance(n, int):
        message = "TypeError: 'n' must be an integer number, not "
        message += type(n).__name__
        return message

    if n <= 0:
        return "ValueError: 'n' must be larger than 0"

    return None
