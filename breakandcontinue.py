# for i in range(1,15):
#     print("5 x", i, "=", 5*i)
#     if(i ==10):
#         break   #same for while loop and break statement leave the whole loop
    
for i in range(1,15,1): #(starting,ending,difference)
    if(i ==10):
        print("skip this iteration")
        continue            # in contioue it just skip that particular iteration
    print("5 x", i, "=", 5*i)
   