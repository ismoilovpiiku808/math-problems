# This is a simple example of generating a sequence of random numbers.
import random

def generate_random_numbers(n):
    """
    Generates n random numbers between 0 and 100.
    
    Args:
        n (int): The number of random numbers to generate.

    Returns:
        list: A list containing the generated random numbers.
    """
    return [random.randint(0, 100) for _ in range(n)]

# Example usage
if __name__ == "__main__":
    n = 5
    result = generate_random_numbers(n)
    print(result)
