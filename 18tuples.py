#tuple use the () round bracket
#list use the [] square bracket


tup1 =[1,3,4,6]  #list
tup1[0]=90
tup2 = (1,3,4,6)  #tuple


print(type(tup1),tup1)  #<class 'list'> [90, 3, 4, 6]
print(type(tup2),tup2)  #<class 'tuple'> (1, 3, 4, 6)



tup3=(1)
tup4=(1,)


print(type(tup3),tup3)  #<class 'int'> 1
print(type(tup4),tup4)  #<class 'tuple'> (1,)


