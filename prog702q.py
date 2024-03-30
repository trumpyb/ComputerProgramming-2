"""
You are to calculate the total number of vehicles.

You are to calculate the total amount that the cars are worth.  

You are to calculate the total amount that the vehicles are worth.  

You are to report the longest home destination name for all of the busses.  

You are to report which truck has the least value.  

You are to report the total number of tires in each of the three classes of vehicles.
"""

def main():
  bus = []
  car = []
  truck = []
  try:
    with open("Dat/Langdat/dataFile.dat", "r") as f:
      while num!=99:
        num = int(f.readline())
        d1 = f.readline()
        d2 = f.readline()
        d3 = f.readline()
        if num==1:
          
        if num==2:
          
        if num==3:
          


  
  except Exception as e:

    print("Error", e)


if __name__=="__main__":
  main()