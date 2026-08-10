s1 ={1,2,3,4,5}
s2={3,4,5,6,7}

# print(s1.union(s2))   #{1, 2, 3, 4, 5, 6, 7}

# print(s1,s2)   #{1, 2, 3, 4, 5}    {3, 4, 5, 6, 7}

# s1.update(s2)   #the missing values in s1 which is present in s2 will add in to the s1 set

# print(s1,s2)   #{1, 2, 3, 4, 5, 6, 7}     {3, 4, 5, 6, 7}


# s3=s1.intersection(s2)
# print(s3)   #{3, 4, 5} common in both sets


s1.intersection_update(s2)


print(s1)  #{3, 4, 5} it will give the common and update the s1.