print("Welcome to Temperature Converison!")
print()

unit = input("Is this temperature in Celsius or Fahrenheit (chose F or C)?: ")
temp = float(input("What is the unit you currenly have?: "))

if unit == "C":
  math = (temp * 1.8) + 32
  print(f"Your temperature in Fahrenheit is: {math}")
if unit == "F":
  math = (temp - 32) * 1.8
  print(f"Your temperature in Celsius is: {math}")
else:
  print("Somethings wrong try again...")