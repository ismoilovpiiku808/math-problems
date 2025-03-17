import random 
def generate_random_python_code(): 
    # Generate a random number between 1 and 50 
    num = random.randint(1, 50) 
    # Generate a random operator (+, -, *, /) 
    op = random.choice(['+', '-', '*', '/']) 
    # Generate a random number between 1 and 50 
    num2 = random.randint(1, 50) 
    # Evaluate the expression using the given operator 
    result = eval(f"{num} {op} {num2}") 
    return f"{num} {op} {num2} = {result}"