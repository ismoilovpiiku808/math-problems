def get_random_math_problem(n=10):
    numbers = list(range(1, n+1))
    problem = ""
    for i in range(n):
        num1 = random.choice(numbers)
        num2 = random.choice(numbers)
        numbers.remove(num1)
        numbers.remove(num2)
        op = random.choice(["+", "-", "*", "/"])
        problem += f"{num1} {op} {num2}"
    return problem
