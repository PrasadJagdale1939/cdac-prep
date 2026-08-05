marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[:])#default length of list
# print(marks[1:9])
# print(marks[1:9:3])#(start,end, jumping index)

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst) 

# lst1 = [1,2,2,3,5,4,6]
# lst2 = ["Red", "Green", "Blue"]
# print(lst1) #[1, 2, 2, 3, 5, 4, 6]
# print(lst2) #['Red', 'Green', 'Blue']



# details = ["Abhijeet", 18, "FYBScIT", 9.8]
# print(details)  #['Abhijeet', 18, 'FYBScIT', 9.8]



# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# #          [0]      [1]     [2]      [3]      [4]


# #positive indexing
# print(colors[2])  #Blue
# print(colors[4])  #Green
# print(colors[0])  #Red

# #negative indexing
# print(colors[-1])  #green   #colors[len(colors)-1]
# print(colors[-3])  #blue    #colors[len(colors)-3]
# print(colors[-5])  #red     #colors[len(colors)-5]



# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#     print("Yellow is present.")  #Yellow is present.
# else:
#     print("Yellow is absent.")



# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Orange" in colors:
#     print("Orange is present.")
# else:
#     print("Orange is absent.")  #Orange is absent.



# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[3:7])	#using positive indexes   #['mouse', 'pig', 'horse', 'donkey']
# print(animals[-7:-2])	#using negative indexes'   #['bat', 'mouse', 'pig', 'horse', 'donkey']



# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[4:])	#using positive indexes    #['pig', 'horse', 'donkey', 'goat', 'cow']
# print(animals[-4:])	#using negative indexes    #['horse', 'donkey', 'goat', 'cow']



# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[:6])	#using positive indexes  #['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
# print(animals[:-3])	#using negative indexes  #['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']



# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[::2])		#using positive indexes   #['cat', 'bat', 'pig', 'donkey', 'cow']
# print(animals[-8:-1:2])	#using negative indexes   #['dog', 'mouse', 'horse', 'goat']



# animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
# print(animals[1:8:3])   #['dog', 'pig', 'goat']   #listName[start : end : jumpIndex]



# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)    #['Milo', 'Bruno', 'Rosa']




names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)