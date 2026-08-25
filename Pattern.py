n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    for j in range(i):
        char = chr(65 + (2 * j))
        print(char, end=" ")
    
    print()
