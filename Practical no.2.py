# Program to implement different operators in Python

a = 10
b = 5

# Arithmetic Operators
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# Relational Operators
print("\nRelational Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 10:", a > 5 and b < 10)
print("a > 15 or b < 10:", a > 15 or b < 10)
print("not(a > b):", not(a > b))

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

# Assignment Operators
print("\nAssignment Operators:")
x = 10
print("Initial x:", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x //= 4
print("x //= 4:", x)