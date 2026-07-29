#Strings are immutable
a = "!!!!! Prasad!!!!! Prasad !!!!!Prasad Prasad Prasad !!"

print(len(a)) #53
print(a.upper())  #!!!!! PRASAD!!!!! PRASAD !!!!!PRASAD PRASAD PRASAD !!
print(a.lower())  #!!!!! prasad!!!!! prasad !!!!!prasad prasad prasad !!

#it do not effect on leding symbols.
print(a.rstrip("!"))  #!!!!! Prasad!!!!! Prasad !!!!!Prasad Prasad Prasad 

#it do  not change the main source
print(a.replace("Prasad", "Jagdale"))  #!!!!! Jagdale!!!!! Jagdale !!!!!Jagdale Jagdale Jagdale !!

#split() gives output in list form
print(a.split(" "))  #['!!!!!', 'Prasad!!!!!', 'Prasad', '!!!!!Prasad', 'Prasad', 'Prasad', '!!']


#Capitalize()
blogHeading = "welcome tO mY VlOg"
print(blogHeading.capitalize())  #Welcome to my vlog


#Center()
str1 = "Welcome to my Vlog  0"
print(len(str1))  #21
print(str1.center(50))   #"Welcome to my Vlog  0 " -> but in the center 
print(len(str1.center(50))) #50


#Count()
print(a.count("Prasad")) #5


#endswith() -> Always in boolean 
print(str1.endswith("log")) #false
print(str1.endswith("log", 15,18)) #true
print(str1.endswith("log", 15,17)) #false


#find()
print(str1.find("my")) #11
print(str1.find("myhhh")) #-1

#index()
print(str1.index("my"))  #11
# print(str1.index("myhhh"))   -> It will threw an error !

#isalnum()
str1 = "WelcometomyVlog0"
print(str1.isalnum())  #True
print(str1)  #WelcometomyVlog0

#isalalpha
str1 ="welcome" 
str2 ="welcome00" 
print(str1.isalpha()) #True
print(str2.isalpha()) #False


