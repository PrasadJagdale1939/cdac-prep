# # f-string -> Formatted string literal
# # the modern, standard way to embed variables and expressions directly inside Python strings.


# name = "Prasad"
# age = 22

# # Basic variable embedding
# print(f"My name is {name} and I am {age} years old.") # Output: My name is Alice and I am 25 years old.


##-> Evaluate Expressions and Math


# print(f"Next year, you will be {age + 1}.") # Output: Next year, you will be 26.

# print(f"Uppercase name: {name.upper()}") # Output: Uppercase name: ALICE



##-> Format Numbers and Decimals

# pi = 3.14159
# price = 1000000

# # Round float to 2 decimal places
# print(f"Pi: {pi:.2f}")          # Output: Pi: 3.14

# # Add commas as thousands separators
# print(f"Cost: ${price:,}")       # Output: Cost: $1,000,000


##-> Inline Debugging (Python 3.8+)

# x = 10
# y = 25

# print(f"{x=}, {y=}, {x+y=}") # Output: x=10, y=25, x+y=35

# print(f"{x}, {y}, {x+y}") # Output: 10, 25, 35


##-> Working with Dictionaries

# user = {"name": "Prasad", "role": "Admin"}

# # Double quotes outside, single quotes inside
# print(f"User {user['name']} is an {user['role']}.") # Output: User Prasad is an Admin.


##-> Padding and Alignment

text = "test"
print(f"{text:>10}")   # Right-align (width 10): '      test'
print(f"{text:<10}")   # Left-align (width 10):  'test      '
print(f"{text:^10}")   # Center-align (width 10): '   test   '

