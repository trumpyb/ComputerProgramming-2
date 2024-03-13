from CL213f import *

def main():
  try:
    elecbills = []
    with open("Dat/Langdat/prog213f.dat", "r") as f:
      for line in f:
        kwh = int(line)
        if kwh!=-999:
          bill = Cl213f(kwh)
          elecbills.append(bill)
    for bill in elecbills:
      bill.calc()
      print(bill)
        
  except Exception as e:

    print("Error", e)


if __name__=="__main__":
  main()