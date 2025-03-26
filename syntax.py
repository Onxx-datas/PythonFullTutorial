"""
Python Syntax Tutorial
=======================
This script covers basic Python syntax, including:
- Indentation
- Conditional statements
- Comparison operators
- Variable declaration
- Printing output
- elif and else statements
- Invalid syntax examples
"""

# Indentation is important in Python. Blocks of code must be properly indented.
if 10 > 5:  # This is a correct indentation
    print("Ten is greater than five")  # This line is inside the if-statement block

# Conditional Statements & Comparison Operators
if 10 > 3:  # Greater than operator
    print("Ten is greater than three")

if 3 > 1:  # Another comparison example
    print("Three is greater than 1")

# Variable Declaration
# In Python, variables do not need explicit type declarations

a = 7  # Integer variable
b = "Python is easy"  # String variable
print(a, b)  # Print multiple values
print("Hello, Python!")  # Printing a simple string

# Using elif and else statements
num = 15
if num > 20:
    print("Number is greater than 20")
elif num > 10:  # Runs if the previous condition is False
    print("Number is greater than 10 but not more than 20")
else:  # Runs if all previous conditions are False
    print("Number is 10 or less")

# Example of Invalid Syntax
# Uncommenting the below code will raise an indentation error
# if 5 > 3:
# print("This will cause an IndentationError")  # Incorrect indentation

# Uncommenting the below code will cause a SyntaxError due to missing colon
# if 10 > 2
#     print("Missing colon at the end of the if statement")

# Uncommenting the below code will cause a TypeError
# print("String" + 5)  # Cannot concatenate a string with an integer without conversion
# Correct way:
print("String " + str(5))  # Convert integer to string before concatenation