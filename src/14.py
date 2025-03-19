import random

def get_random_math_problem():
    """
    Generates a random math problem of the form "x + y = z" where x, y, and z are integers between 1 and 10.
    Returns:
        A tuple (x, y, z) representing the solution to the math problem.
    """
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = x + y
    return (x, y, z)