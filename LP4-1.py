copies = int(input("Enter Number of copies to be printed: "))

price = 0.0

if 0 < copies <=99:
  price = 0.30
elif 99 < copies <= 499:
  price = 0.28
elif 499 < copies <= 749:
  price = 0.27
elif 749 < copies <= 1000:
  price = 0.26
elif copies >1000:
  price = 0.25
else:
  print("Number Of Copies is Invalid")
  exit()

print("Price per copy is : $"+str(price))
print("Total cost is: $"+str(price*copies))