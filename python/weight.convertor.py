k_p = input("What weight are you inputting Kilograms or Pounds(Choose K or P): ")
weight = int(input("Now input the weight you want: "))

if k_p.upper == 'P':
  total = weight / 2.205
  print(f"Your weight in kilograms is {round(total)}")
elif k_p.upper == 'K':
  total = weight * 2.205
  print(f"Your weight in kilograms is {round(total)}")
else:
  print("Somethings went wrong please try again...")