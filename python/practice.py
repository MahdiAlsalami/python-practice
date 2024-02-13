'''print('Weight Converter(Pounds -> Kilograms)')

weight = int(input("What is your weight in pounds: "))

kilo = weight * 0.453592

print(f"Your weight in kilograms is {kilo}")'''


high_income = True
good_credit = True

if high_income and good_credit:
  print("Eligible for loan")
elif high_income == True and good_credit ==False:
  print("Not eligible for loan")
elif high_income == False and good_credit == True:
  print("Not eligible for loan")
elif high_income == False and good_credit == False:
  print("Not eligible for loan")
else:
  print("Have a good day!")


