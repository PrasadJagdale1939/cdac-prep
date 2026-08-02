def calculateGmean(a,b):
    mean =(a*b)/(a+b)
    print(mean)
    

def isGreater(a,b):
    if(a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")
        

a = 9
b = 18

calculateGmean(a,b) #6.0
isGreater(a,b) #b is greater than a



def example(parameters):
    pass  # it allows us to leave the empty function body for future changes other wise it will give an error. 