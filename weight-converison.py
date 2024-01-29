print("Welcome to Mahdi's Weight Convertor!")

weight_option = input("Choose (P) for pounds if you want to convert to that or choose (K) for kilograms: ")

if weight_option == "P":
  kilo = float(input("Enter weight of kilograms: "))
  total = kilo * 2.205
  print(f"Your weight in pounds is: {round(total, 2)}")
elif weight_option == "K":
  pound = float(input("Enter weight of pounds: "))
  total = pound / 2.205
  print(f"Your weight in kilograms is: {round(total, 2)}")
else:
  print("Somethings wrong try again...")