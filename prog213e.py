
distr = [0]*5
len = 0

with open("Dat/Langdat/prog213e.dat","r") as f:
  for age in f:

    age = int(age)

    len += 1
    
    if age < 20:
      distr[0] += 1
    if 20 <= age <= 39:
      distr[1] += 1
    if 40 <= age <= 59:
      distr[2] += 1
    if 60 <= age <= 79:
      distr[3] += 1
    if age > 79:
      distr[4] += 1
    

for x in distr:
  print(x/len)