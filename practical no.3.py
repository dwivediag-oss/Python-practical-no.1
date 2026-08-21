# Program to perform operations on Python lists

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Adding elements
numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

# Removing elements
numbers.remove(25)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

# Sorting
numbers.sort()
print("After sort:", numbers)

# Reversing
numbers.reverse()
print("After reverse:", numbers)

# Built-in list functions
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))
print("Count of 20:", numbers.count(20))