s1 ={1,2,3,4,5}
s2={3,4,5,6,7}
s3={1,2,3}
s4=set()

# print(s1.union(s2))   #{1, 2, 3, 4, 5, 6, 7}

# print(s1,s2)   #{1, 2, 3, 4, 5}    {3, 4, 5, 6, 7}

# s1.update(s2)   #the missing values in s1 which is present in s2 will add in to the s1 set

# print(s1,s2)   #{1, 2, 3, 4, 5, 6, 7}     {3, 4, 5, 6, 7}


####################################################################

# s3=s1.intersection(s2)
# print(s3)   #{3, 4, 5} common in both sets


# s1.intersection_update(s2)

# print(s1)  #{3, 4, 5} it will give the common and update the s1.



###################################################################

# s4= s1.symmetric_difference(s2)

# print(s4)    #{1, 2, 6, 7}  it will print the uncommon values



# s1.symmetric_difference_update(s2)

# print(s1)  #{1, 2, 6, 7}  it will print the uncommon values and also change the original set s1


###################################################################


# print(s1.isdisjoint(s2))   #False . because it has common sharing values in it


# print(s1.issuperset(s3)) #True . because the s1 is having all the values of s3. 


# print(s3.issubset(s1))  #True . because it just opposite of superset


####################################################################


# s4.add(8)  #it will just add 8 (only single element) into the s4 empty set 
# print(s4)  #{8}


####################################################################

# print(s2)   #{3, 4, 5, 6, 7}

# s2.remove(3)  # remove will raise the error if element not found

# print(s2)   #{4, 5, 6, 7}

#################################################################


# print(s2)   #{3, 4, 5, 6, 7}

# s2.discard(3)  #it will work as same as remove but discard will not raise the error if element not found 

# print(s2)   #{4, 5, 6, 7}

##################################################################


# random = s1.pop()   # it will pop the last item from the set , as set are unordered so we dont know what will pop 

# print(random)    

####################################################################


# del s1  #for deleting the entire set

# print(s1)  #it will give us error that s1 is not defined because we delete it by del s1


#######################################################################

# s1.clear()   #it will clear the items from set instead of entire set
# print(s1)   #it will give empty set () or set()


########################################################################

# if 7 in s2:
#     print("Yes it is present")   #Yes it is present
# else:
#     print("No it is not present")

########################################################################

