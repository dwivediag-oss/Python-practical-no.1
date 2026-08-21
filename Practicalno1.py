# Student Data System

# Taking input from user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))

# Boolean data type
is_pass = percentage >= 40

# Displaying student information
print("\n--- Student Data ---")
print("Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)
print("Percentage:", percentage)
print("Pass Status:", is_pass)

# Displaying data types
print("\n--- Data Types ---")
print("Name data type:", type(name))
print("Roll number data type:", type(roll_no))
print("Age data type:", type(age))
print("Percentage data type:", type(percentage))
print("Pass status data type:", type(is_pass))