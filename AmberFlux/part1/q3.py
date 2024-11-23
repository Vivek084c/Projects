import math

def lcm(a, b):
    """
    Compute the Least Common Multiple (LCM) of two numbers using the GCD method.

    :param a: First integer
    :param b: Second integer
    :return: LCM of a and b
    """
    return abs(a * b) // math.gcd(a, b)

# Example usage
num1 = 12
num2 = 18
print("LCM of", num1, "and", num2, "is:", lcm(num1, num2))