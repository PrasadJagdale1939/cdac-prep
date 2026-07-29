#Strings are immutable
a = "!!!!! Prasad!!!!! Prasad !!!!!Prasad Prasad Prasad !!"

print(len(a))
print(a.upper())
print(a.lower())

#it do not effect on leding symbols.
print(a.rstrip("!"))

#it do  not change the main source
print(a.replace("Prasad", "Jagdale"))

#split() gives output in list form
print(a.split(" "))


#Capitalize()
blogHeading = "welcome tO mY VlOg"
print(blogHeading.capitalize())


#Center()
str1 = "Welcome to my Vlog"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))


#Count()
print(a.count("Prasad"))


#endswith() -> Always in boolean 
print(str1.endswith("log"))
print(str1.endswith("log", 15,18))
print(str1.endswith("log", 15,17))

