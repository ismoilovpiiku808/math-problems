import random

def get_random_math_problem():
    numbers = list(range(1, 101))
    operation = random.choice(['+', '-', '*'])
    problem = f"{random.choice(numbers)}{operation}{random.choice(numbers)}={}"
    return problem
