l = [51,34,44,55,56,67,18]

# print(l)   #[51, 34, 44, 55, 56, 67, 18]



# l.reverse()
# print(l)   #[18, 67, 56, 55, 44, 34, 51] its reverse the original list



# l.append(10) # its push the new number in the ned of the list



# l.sort()   #its arrange the numbers in asending order
# print(l)   #[10, 18, 34, 44, 51, 55, 56, 67]




# l.sort(reverse=True)   #its arrange the numbers in desending order
# print(l)   #[67, 56, 55, 51, 44, 34, 18, 10]



# print(l.index(55))   #3  it is a position of 55.


# print(l.count(55))  #1 occurance of 55 is 1 time in list




# m = l  #this is not good practice unless you know it will change the main list items
# m[0]=0
# print(l)  #[0, 34, 44, 55, 56, 67, 18]



# m = l.copy()  #use copy method which makes a copy of main list
# m[0]=0
# print(l)   #[51, 34, 44, 55, 56, 67, 18]
# print(m)   #[0, 34, 44, 55, 56, 67, 18]



# l.insert(1,899)
# print(l)    #[51, 899, 34, 44, 55, 56, 67, 18]



# m=[799,499,599]
# k=[299,399,199]



# f = m+k+l
# print(f)   #[799, 499, 599, 299, 399, 199, 51, 34, 44, 55, 56, 67, 18]




# l.extend(m)
# print(l)    #[51, 34, 44, 55, 56, 67, 18, 799, 499, 599]  #it just add the m into the l.
