# def avg(a=5,b=6):  #default argument 
#     print("The avg is ",(a+b)/2)

# avg()    #(5+6)/2 = 5.5

# avg(2,3) #2.5

# avg(9) #7.5

# avg(b=9) #7


# avg(b=21,a =55)#keyword argument



# def avg(a,b=6):  #Required argument. a need to give.
#     print("The avg is ",(a+b)/2)
    

       
# def avg(*numbers):  #tuple data type(1,2,3,4,5,6)
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is ",sum/len(numbers))


 
# def name(**name):
#     print("Hello", name["fname"],name["mname"],name["lname"])

# name(mname="Dattatray",fname="Prasad",lname="Jagdale" )    


def avg(*numbers): 
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c = avg(5,6,8,9,10)
print(c)