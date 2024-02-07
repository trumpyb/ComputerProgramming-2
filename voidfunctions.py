from calcfunctions import *

def do_something():
  print("Hello, world!")

def print_nums():
  x = 0
  while x < 10:
    print("x:",x)
    x+=1

def main():
  do_something()
  print_nums()
  a = add(1,2)
  q,r = divmod2(5,10)

  print(q,r)
  

  
  pass


if __name__=="__main__":
  main()