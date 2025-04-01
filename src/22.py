import random

def simple_random_number_generator(min_value: int = 1, max_value: int = 100) -> int:
    """
    Generates a simple random number between 'min_value' and 'max_value'.
    
    Example usage:
    >>> random_number = simple_random_number_generator()
    print(random_number)
    """
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    # You can change the values for min_value and max_value as needed
    min_value = 10
    max_value = 50
    random_number = simple_random_number_generator(min_value=min_value, max_value=max_value)
    print(f"Random number between {min_value} and {max_value}: {random_number}")
