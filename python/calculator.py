num_1 = float(input("Please enter the first value: "))
num_2 = float(input("Please enter the second value: "))
symbol = input("Please enter the arethmetic operator (*, +, -, /, **, %): ")

if symbol == "*":
  total = num_1 * num_2
  print(f"Answer is: {total}")
elif symbol == "+":
  total = num_1 + num_2
  print(f"Answer is: {total}")
elif symbol == "-":
  total = num_1 - num_2
  print(f"Answer is: {total}")
elif symbol == "/":
  total = num_1 / num_2
  print(f"Answer is: {total}")
elif symbol == "**":
  total = num_1 ** num_2
  print(f"Answer is: {total}")
elif symbol == "%":
  total = num_1 % num_2
  print(f"Answer is: {total}")
else:
  print("Somethings wrong try again...")

