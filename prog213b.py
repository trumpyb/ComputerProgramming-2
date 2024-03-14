"""
0	-	99	$5.95
100	-	199	$5.75
200	-	299	$5.40
300 	&	 up	$5.15
"""

with open("Dat/Langdat/prog213b.txt", "r") as f:
  for x in f:
    quantity = int(x)
    price = 0
    
    if quantity <= 99:
      price = 5.95 * quantity
    elif 100 <= quantity <=199:
      price = (5.95*99) + (quantity-99)*5.75
    elif 200 <= quantity <= 299:
      price = (5.96*99)+(5.75*100)+(quantity-199)*5.40
    elif quantity > 300:
      price = (5.96*99)+(5.75*100)+(5.40*100)+(quantity-299)*5.15
  
    print(f"Price: {round(price,2)}")
