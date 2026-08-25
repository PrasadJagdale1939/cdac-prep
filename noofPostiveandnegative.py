num = int(input("Enter a positive integer: "))

sum_even = 0
sum_odd = 0

while num > 0:
    last_digit = num % 10
    
    if last_digit % 2 == 0:
        sum_even += last_digit
    else:
        sum_odd += last_digit

    num = num // 10

print("Sum of even digits =", sum_even)
print("Sum of odd digits =", sum_odd)