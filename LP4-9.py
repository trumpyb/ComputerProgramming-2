import random

guess = input("Enter a number between 1 and 20: ")

compnum = random.randint(1,20)

print("Computers Number: ",compnum)
print("Your Guess: ",guess)

if guess==compnum:
  print("You Won!")
else:
  print("Better Luck Next Time!")