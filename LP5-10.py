num1 = int(input("Input a number: "))
num2 = int(input("Input a second number: "))

while num2>0:
  temp = num1%num2
  num1=num2
  num2=temp

print(num1)