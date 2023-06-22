"""
Sum Calculator Module
=====================

    Calculate the sum of numbers in the given list of lines.

    Args:
        lines (list): A list of strings representing numeric values.

    Returns:
        int: The sum of the numeric values in the given lines.

    Raises:
        ValueError: If any of the lines cannot be converted to an integer.

"""
def calculate(lines):
    total = 0
    try:
        for line in lines:
            total += int(line.strip())
        return total
    except ValueError as e:
        raise ValueError("Invalid literal for int() with base 10") from e