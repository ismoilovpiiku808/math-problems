def add_numbers(a: float, b: float) -> float:
    """
    Adds two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """
    Subtracts the second number from the first number.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The result of the subtraction.
    """
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of the two numbers.
    """
    return a * b

def divide_numbers(a: float, b: float) -> float:
    """
    Divides one number by another.

    Parameters:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float: The result of the division.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")

def find_max(numbers: list) -> float:
    """
    Finds the maximum number in a list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The maximum number in the list.
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty.")
    
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number

def find_min(numbers: list) -> float:
    """
    Finds the minimum number in a list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The minimum number in the list.
    """
    if len(numbers) == 0:
        raise ValueError("The list is empty.")
    
    min_number = numbers[0]
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number

# Example usage
num1 = add_numbers(5, 3)
num2 = subtract_numbers(4.5, 2.5)
print(num1)  # Output: 8.0
print(num2)  # Output: 2.0
