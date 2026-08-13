###ValueError using the raise keyword. This exception is typically used 
## when a function receives an argument of the correct data type but with 
## an inappropriate value

a = input("Enter any value between 5 and 9 : ")

# 1. Check for the string "quit" first
if a == "quit":
    print("program executed successfully")
else:
    # 2. Convert the input to an integer
    a = int(a) 
    
    # 3. Now you can safely check the numbers
    if a < 5 or a > 9:
        raise ValueError("Value should be between 5 and 9")
    else:
        print("The given Number is ", a)