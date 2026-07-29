#Strings are immutable
a = "!!!!! Prasad!!!!! !!!!! !!"

print(len(a))
print(a.upper())
print(a.lower())

#it do not effect on leding symbols.
print(a.rstrip("!"))

#it do  not change the main source
print(a.replace("Prasad", "Jagdale"))

#
print(a.split(" "))

#Capitalize()

blogHeading = "welcome tO mY VlOg"
print(blogHeading.capitalize())

