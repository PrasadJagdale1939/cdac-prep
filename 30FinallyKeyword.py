###In Python, the finally keyword defines a block of code that always executes, 
# regardless of whether an exception is raised or caught. It is used within 
# try...except structures primarily for resource cleanup

def func1():
    try:
         # Code that might cause an error
        l = [1, 5, 6, 7]
        i =int(input("Enter the index: "))
        print(l[i])
        return 1
    
    except:
        # Handles specific error
        print("Some error occurred")
        return 0
    
    finally:
        # Always runs to clean up resources
        print("I am always executed")
        
x = func1()
print(x)