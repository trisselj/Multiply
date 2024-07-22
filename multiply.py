# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/17/2024
# Description: Multiplies two numbers together by using recurring addition instead of the built in multiplication

# Defines function as multiply, returns the product of two integers using recursion
def multiply(a, b):
    if b == 1: # Returns "a" if multiply by one
        return a
    return a + multiply(a, b - 1) # Generates recursion: a * b = a + (a * (b - 1))
