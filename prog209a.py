with open("Dat/Langdat/prog215a.dat", "r") as f:
  total = 0
  less = 0
  equal = 0
  more = 0
  for x in f:
    total += 1
    x = int(x)

    if x < 500:
      less += 1
    if x == 500:
      equal += 1
    if x > 500:
      more += 1

print(f"The numbers less than 500: {less}")
print(f"The numbers equal to 500: {equal}")
print(f"The numbers more than 500: {more}")
print(f"Total: {total}")