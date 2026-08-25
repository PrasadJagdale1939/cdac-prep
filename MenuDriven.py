while True:
  print("=====Canteen Menu=====")
  print("1. Tea (₹10)")
  print("2. Coffee (₹15)")
  print("3. Water (₹5)")
  print("4. Bunmuska (₹20)")
  print("==================")


  choice = int(input("Enter Your Choice : "))
  bill = 0

  tea = 10
  coffee = 15
  water = 5
  bunmuska = 20

  match choice:
    case 1:
      quantity = int(input("Enter Quantity : "))
      print(f"Item : Tea")
      print(f"Quantity : {quantity}")
      print(f"Rate : {tea}")
      print(f"Total Amount: {tea*quantity}")
      print(f"Thank you! Visit again.")
      print("==================")
    case 2:
      quantity = int(input("Enter Quantity : "))
      print(f"Item : Coffee")
      print(f"Quantity : {quantity}")
      print(f"Rate : {coffee}")
      print(f"Total Amount: {coffee*quantity}")
      print(f"Thank you! Visit again.")
      print("==================")
    case 3:
      quantity = int(input("Enter Quantity : "))
      print(f"Item : Water")
      print(f"Quantity : {quantity}")
      print(f"Rate : {water}")
      print(f"Total Amount: {water*quantity}")
      print(f"Thank you! Visit again.")
      print("==================")
    case 4:
      quantity = int(input("Enter Quantity : "))
      print(f"Item : Bunmuska")
      print(f"Quantity : {quantity}")
      print(f"Rate : {bunmuska}")
      print(f"Total Amount: {bunmuska*quantity}")
      print(f"Thank you! Visit again.")
      print("==================")
    case _:
      print("Invalid Input, Enter a Vailid Menu Number !")
