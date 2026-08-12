# dic = {
#     "Prasad": "Human",
#     "Spoon": "Object"
# }

# print(dic["Prasad"])  # Human

#################################################################

# dic1 = {
#     123: "Prasad",
#     235:"Spoon"
# }
# print(dic1[123])   #Prasad

##################################################################

info ={"name":"Prasad", "age":22,"eligible":True}

# print(info)  #{'name': 'Prasad', 'age': 22, 'eligible': True}

# print(info.keys())   #dict_keys(['name', 'age', 'eligible'])

# print(info.values())    #dict_values(['Prasad', 22, True])

##################################################################

# print(info["name"])    #Prasad
# print(info.get("name"))   #Prasad

#################################################################
##if we put the non existed then it will throw an error

# print(info["name2"])    #ERROR

# print(info.get("name2"))   #but it will give None instead of ERROR

#################################################################

# for key in info.keys():
#     print(info[key])   #Prasad 22 True
    

for key in info.keys():
    print(f"The Value Corresponding to the key {key} is {info[key]}")










