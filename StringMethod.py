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


#islower()
str1 ="welcome" 
str2 ="WELCOME"

print(str1.islower()) #true
print(str2.islower()) #false

#isupper()
print(str1.isupper()) #false
print(str2.isupper()) #true


#isprintable()
str1 = "WelcometomyV\nlog0"
str2 = "WelcometomyVlog0"
print(str1)

print(str1.isprintable()) #false
print(str2.isprintable()) #true


#isspace()

str1 = "Welcome to my Vlog"
print(str1.isspace())   #false
str2 = "Welcome to  my  Vlog"
print(str2.isspace())    #false


str1 = "           "
print(str1.isspace()) #true
str2 = "                    "
print(str2.isspace()) #true

#istitle()
str1 = "Prasad Dattatray Jagdale"
str2 = "Prasad dattatray jagdale"

print(str1.istitle()) #true
print(str2.istitle()) #false


#startswith()
str1="Hey, I Am New Here !"
print(str1.startswith("python")) #false
print(str1.startswith("Hey, I")) #true


#swapcase1()
print(str1.swapcase())  #hEY, i aM nEW hERE !  ## its just swap the cases

#title()
str1= "his name is prasad. prasad is an honest man"
print(str1.title())  #His Name Is Prasad. Prasad Is An Honest Man