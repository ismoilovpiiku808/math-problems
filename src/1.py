def get_random_math_problem(a=1, b=10):
    op = ['+', '-', '*', '/'][randint(0, 3)]
    x = randint(a, b)
    y = randint(a, b)
    if op == '+':
        return f'{x} {op} {y}'
    elif op == '-':
        return f'{x} - {y}'
    elif op == '*':
        return f'{x} * {y}'
    else:
        return f'{x} // {y}'
