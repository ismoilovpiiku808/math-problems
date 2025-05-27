import math

def calculate_square_root(num):
    """Calculate the square root of a given number."""
    return math.sqrt(num)

if __name__ == "__main__":
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
