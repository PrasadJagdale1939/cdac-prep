# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5)) #36,28,800

#funtion Calls itself within the same fundtion.
#  5 * factorial(4) 
#  5 * 4* factorial(3) 
#  5 * 4 * 3 factorial(2) 
#  5 * 4 * 3* 2 factorial(1) 
#  5 * 4 * 3 * 2 * 1  -> 120



#Fibonacci series in Python
# f0 = 0
# f1 = 1
# f2 =f1 + f0
# f(n) = f(n-1) + f(n-2)


# def fibonacci_fast(n):
#     if n == 0:
#         return 0
    
#     # Corrected simultaneous assignment
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
        
#     return b

# # Test cases
# print(fibonacci_fast(0))
# print(fibonacci_fast(1))
# print(fibonacci_fast(2))
# print(fibonacci_fast(3))
# print(fibonacci_fast(4))
# print(fibonacci_fast(100))
# print(fibonacci_fast(1000)




# Good practice: clearly shows the index isn't used
for i in range(3):
    print("Hello")

for _ in range(3):
    print("Hello")


for i in range(3):
    print(f"This is loop number {i}")

#If you use i, Python creates a variable that holds the numbers 0, 1, and 2 on each turn of the loop.
# This is loop number 0
# This is loop number 1
# This is loop number 2



for _ in range(3):
    print("Hello")# 'i' is gone, we don't care about the 0, 1, or 2 

# Hello
# Hello
# Hello