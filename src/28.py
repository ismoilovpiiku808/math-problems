def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    """Subtract one number from another."""
    return a - b

def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def divide_numbers(a: int, b: int) -> float:
    """Divide one number by another."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
