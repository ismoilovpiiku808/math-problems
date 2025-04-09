def max_product_of_three(nums):
    """
    Find the maximum product of any three numbers from the given list.
    
    Args:
        nums: A list of integers
    
    Returns:
        The maximum product of any three numbers in the list.
    """
    nums.sort()
    n = len(nums)
    if n < 3 or n % 2 == 1:
        return None
    a, b, c = nums[0], nums[1], nums[n-1]
    return max(a * b * c, (nums[0] * nums[1]) * nums[n-1])

# Example usage and check function
def check_max_product_of_three():
    test_cases = [
        ([5, -6, 2, -1]),  # Output: -30
        ([4, -2, 8, -6, 3, -1]),  # Output: 72 (max of (-6) * (-1) * 3)
    ]
    
    for nums in test_cases:
        result = max_product_of_three(nums)
        assert result is not None and result == 72, f"Expected {72}, got {result}"
        print(f"Passed: max_product_of_three({nums}) = {result}")

check_max_product_of_three()
