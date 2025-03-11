import random

def get_random_math_problem(a=1, b=10):
    op = random.choice(['+', '-', '*', '/'])
    problem = f"{a} {op} {b}"
    return problem

print(get_random_math_problem())
