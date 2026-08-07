# countries = ("india","europe","USA","UAE")  #tuple
# temp = list(countries)    #tuple stored in temp as list format
# temp.append("russia")     #we add item
# temp.pop(1)               #we remove item
# temp[2]="finland"         #we change item
# countries= tuple(temp)    #converted tuple in to list , is now again convert into the tuple.
# print(countries)          #print the changed tuple    #('india', 'USA', 'finland', 'russia')




countries1 =("pakistan","afganistan","bangladesh")
countries2 =("vietnam","india","china")

southEastAsia = countries1 + countries2
print(southEastAsia)   #('pakistan', 'afganistan', 'bangladesh', 'vietnam', 'india', 'china')