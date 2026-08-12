ep1 ={ 122:45,52:34,367:70}

ep2={653:44,564:78}


# ep1.update(ep2)  #it will update the ep1 by adding key values of ep2 in ep1

# print(ep1)  #{122: 45, 52: 34, 367: 70, 653: 44, 564: 78}

# print(ep2)  #{653: 44, 564: 78}

# ep1.clear()
# print(ep1)  #{}  ->empty dictionary


# empt ={}
# print(empt)  #{}  ->empty dictionary


##########################################################

# ep1.pop(122)
# print(ep1)    #{52: 34, 367: 70} ---> it has deleted the (122:45)key value pair


# ep1.popitem()   #it will pop last key value pair from the dictionary
# print(ep1)    #{122: 45, 52: 34}

###########################################################

# del ep1  #it will delete the whole dictionary
# print(ep1) # it will throw an error

# del ep1[122]  #it will delete only 122 key with pair
# print(ep1) # {52: 34, 367: 70}

##############################################################














