import random
num = int(input("Enter a Number "))

jackpot = random.randint(1,100)
count = 1

while num != jackpot:
  if num > jackpot:
    print("Guess lower !")
  else:
    print("Guess Higher !")
  num = int(input("Enter a Number Again "))
  count+=1

print(f"You won the Game You took {count} Attempt")

