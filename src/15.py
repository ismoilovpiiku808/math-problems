import random

def get_random_math_problem():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(operators)
    if operator == '+':
        return f'{num1} + {num2}'
    elif operator == '-':
        return f'{num1} - {num2}'
    elif operator == '*':
        return f'{num1} * {num2}'
    else:
        return f'{num1} / {num2}'
