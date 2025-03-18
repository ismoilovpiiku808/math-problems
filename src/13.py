 import random

def solve_math_problem(a, b):
    problem = str(random.randint(0, 10)) + " x " + str(random.randint(0, 10)) + " = ?"
    answer = a * b
    return problem, answer