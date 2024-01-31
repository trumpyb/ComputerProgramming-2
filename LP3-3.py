eggs = int(input("Number of eggs: "))

dozens = eggs // 12
remaining = eggs % 12

dozen_price  = 0.0

if 0 < dozens < 4:
  dozen_price = 0.50
if 4 <= dozens < 6:
  dozen_price = 0.45
if 6 <= dozens < 11:
  dozen_price = 0.40
else:
  dozen_price = 0.35

single_price = (1/12) * dozen_price

total_price = dozens*dozen_price + remaining * single_price

print("Total price: " + str(total_price))

