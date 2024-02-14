
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
  person_guess = int(input("Guess correct number: "))
  guess_count += 1
  if person_guess == secret_number:
    print("Correct!")
    break
else:
  print("You lose.")
  

