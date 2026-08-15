questions =[
    
    ["Which planet is known as the Red Planet?","Earth","Mars","Venus","Jupiter",2],
    ["Who wrote the Indian national anthem \"Jana Gana Mana\"?","Bankim Chandra Chatterjee","Rabindranath Tagore","Mahatma Gandhi","Subhash Chandra Bose",2],
    ["Which animal is known as the Ship of the Desert?","Horse","Elephant","Camel","Donkey",3],
    ["In which year did India win its first Cricket World Cup under Kapil Dev?","1975","1983","1987","2011",2],
    ["Which city is known as the Silicon Valley of India?","Mumbai","Hyderabad","Pune","Bengaluru",4],
    ["Who was the first woman Prime Minister of India?","Pratibha Patil","Sarojini Naidu","Indira Gandhi","Sushma Swaraj",3],
    ["What is the chemical symbol for Gold?","Ag","Au","Pb","Fe",2],
    ["Which is the longest river in the world?","Amazon River","Nile River","Yangtze River","Ganga River",2],
    ["The famous Ajanta Caves are located in which Indian state?","Madhya Pradesh","Bihar","Maharashtra","Odisha",3],
    ["Who invented the World Wide Web (WWW) in 1989?"," Bill Gates","Steve Jobs","Tim Berners-Lee","Mark Zuckerberg",2]
              
            ]


levels =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

i = 0
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print("\n#################################################################################")
    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"\n{question[0]}")
    print(f"\na. {question[1]}                              b.{question[2]}")
    print(f"\nc. {question[3]}                              d.{question[4]}")
    
    reply = int(input("\nEnter your answer (1 - 4) or 0 to quit  "))
    if(reply == 0):
        money = levels[i-1]
        break
    if (reply == question[5]):
        print(f"\nCorrect answer , you have won Rs. {levels[i]}")
        
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("\nWrong answer !")
        break       
    
print   (f"\nYour Take Home Money is {money}\n")
    
    











