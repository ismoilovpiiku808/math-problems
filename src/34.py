import math

def square_root(n):
    return int(math.sqrt(n))

n = float(input("Enter a number: "))
result = square_root(n)
print(f"The square root of {n} is {result}.")
