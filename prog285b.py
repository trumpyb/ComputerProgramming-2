from Cl285b import Salesperson

def main():
  try:
    print("Number\tCode\tSales\tCommission")
    with open("Langdat-20240306T200213Z-001/Langdat/prog285b.dat","r") as f:
      for line in f:
        ldata = line.split(" ")
        id = int(ldata[0])
        code = int(ldata[1])
        sales = float(ldata[2])
        seller = Salesperson(id, code, sales)
        seller.setComm()
        print(seller)
        
  except Exception as e:
    print("Error", e)
    


if __name__=="__main__":
  main()
