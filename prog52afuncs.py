import voidfunctions

def calcArea(len,wid)-> int:
  return len * wid 

def calcPerim(len: int, wid: int)-> int:
  return 2 * len + 2 * wid

def areaperim(len, wid):
  area = calcArea(len,wid)
  perim = calcPerim(len,wid)

  return area, perim

def main():
  voidfunctions.do_something()
  length = int(input("Input length\n"))
  width = int(input("Input Width\n"))

  area,perim = areaperim(length,width)
  print(f"{area}\n{perim}")
  pass


if __name__=="__main__":
  main()
