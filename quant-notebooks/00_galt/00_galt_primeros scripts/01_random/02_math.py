import math
# Constants
print(math.pi)
print(math.e)

# Arround functions
print(math.floor(4.6))
print(math.ceil(4.4))
print(math.trunc(6.7))
print(round(4.6))

# Logarithms
print(math.log(100,10))
e = math.exp(1)
print(math.log(e))


# Greatest Common Divisor and Factorial
print(math.gcd(9, 24))
print(math.factorial(6))


# Is Close
a = 989
b = 1000
tol = 0.05
print(math.isclose(a, b, rel_tol=0.01))