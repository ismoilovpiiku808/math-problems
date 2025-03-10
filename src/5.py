import random

def get_random_python_code():
    # Generate a random integer between 1 and 100
    num = random.randint(1, 100)
    # Generate a random operation (+, -, *, /)
    op = random.choice(["+", "-", "*", "/"])
    # Generate two random numbers between 1 and 100
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    # Use the operation to generate a random math problem
    problem = f"{num1} {op} {num2}"
    return problem