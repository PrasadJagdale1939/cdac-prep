# # f-string -> Formatted string literal
# # the modern, standard way to embed variables and expressions directly inside Python strings.


# name = "Prasad"
# age = 22

# # Basic variable embedding
# print(f"My name is {name} and I am {age} years old.") # Output: My name is Alice and I am 25 years old.


# print(f"Next year, you will be {age + 1}.") # Output: Next year, you will be 26.

# print(f"Uppercase name: {name.upper()}") # Output: Uppercase name: ALICE



pi = 3.14159
price = 1000000

# Round float to 2 decimal places
print(f"Pi: {pi:.2f}")          # Output: Pi: 3.14

# Add commas as thousands separators
print(f"Cost: ${price:,}")       # Output: Cost: $1,000,000
