help = input(">")
print('start - to start the car')
print('stop - to stop the car')
print('quit - to exit')

while help.upper == "help":
  choose = input('>')
  if choose == "start":
    print('Car started...Ready to go!')
  elif choose == "stop":
    print('Car stopped.')
  elif choose == "quit":
    break
  else:
    print("I dont understand that...")