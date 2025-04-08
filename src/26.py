import sys
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    # Find the smallest power of each prime factor
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            factors.append(i)
    
    if n > 2:
        factors.append(int(sqrt(n)))
    
    return factors

def main():
    # Your code here
    
if __name__ == "__main__":
    main()
