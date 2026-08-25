a = int(input("Enter 1st Term : "))
d = int(input("Common Difference : "))
n = int(input("Enter Number of Term : "))

total_sum = 0

for i in range(n):
    term = a + (i * d)
    print(term, end=" ")
    total_sum += term
    
print("\nSum =", total_sum)