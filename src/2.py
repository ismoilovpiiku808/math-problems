def generate_random_math_problem(max_num=10):
    """
    Generates a random math problem with two numbers and an operator (+, -, *, /).

    Args:
        max_num (int, optional): Maximum value for the two numbers. Defaults to 10.

    Returns:
        str: A string representing the math problem.
    """
    num1 = random.randint(1, max_num)
    num2 = random.randint(1, max_num)
    operator = random.choice(["+", "-", "*", "/"])
    if operator == "+":
        return f"{num1} + {num2}"
    elif operator == "-":
        return f"{num1} - {num2}"
    elif operator == "*":
        return f"{num1} * {num2}"
    else:
        return f"{num1} / {num2}"
