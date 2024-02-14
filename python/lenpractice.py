name = input("What is your name: ")

if len(name) < 3:
  print("Name is to short must be more than 3 character long.")
elif len(name) > 50:
  print('Name is too long.')
elif 3 < len(name) < 51:
  print(f"Name looks good[{name}!]")
else:
  print('Goodbye.')