# math_utils.py
# This module provides basic mathematical utilities and constants.

# Define a constant for the value of Pi, used in various mathematical calculations.
PI = 3.14159

def add(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def area_circle(r):
    """
    Calculates the area of a circle using the formula: πr²

    Parameters:
    r (int or float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return PI * (r ** 2)
