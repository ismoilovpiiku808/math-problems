def get_random_math_problem(max_value):
    """
    Returns a random math problem of the form "x + y = ?" where x and y are random integers between 1 and max_value.
    """
    x = random.randint(1, max_value)
    y = random.randint(1, max_value)
    return f"{x} + {y} = ?"
