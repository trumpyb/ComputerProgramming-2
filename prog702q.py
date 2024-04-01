from Cl702q import *
def main():
  busses = []
  cars = []
  trucks = []
  num = 0
  try:
    with open("Dat/Langdat/dataFile.dat", "r") as f:
      while num!=99:
        num = int(f.readline())
        d1 = f.readline()
        d2 = f.readline()
        d3 = f.readline()
        if num==1:
          cars.append(Car(int(d1), d2, int(d3)))
        if num==2:
          trucks.append(Truck(d1, int(d2), int(d3)))
        if num==3:
          busses.append(Bus(d1, int(d2), d3))

    totVehicles = len(cars) + len(trucks) + len(busses)

    totCarWorth = 0
    for x in cars:
      totCarWorth += x.worth

    totVehicleWorth = totCarWorth
    for x in trucks:
      totVehicleWorth += x.worth
    for x in busses:
      totVehicleWorth += x.worth

    longestname = ""
    for x in busses:
      if len(x.hometown) > len(longestname):
        longestname = x.hometown

    leastValue = 10**99
    for x in trucks:
      if x.worth < leastValue:
        leastValue = x.worth

    carTires = 0
    for x in cars:
      carTires += x.numTires

    truckTires = 0
    for x in trucks:
      truckTires += x.numTires

    busTires = 0
    for x in busses:
      busTires += x.numTires
    
    print(f"Total Vehicles: {totVehicles}")
    print(f"Total Car Worth: {totCarWorth}")
    print(f"Total Vehicle Worth: {totVehicleWorth}")
    print(f"Longest Home Name: {longestname}")
    print(f"Truck With Least Value: {leastValue}")
    print(f"Total Car Tires: {carTires}")
    print(f"Total Bus Tires: {busTires}")
    print(f"Total Truck Tires: {truckTires}")
  
  except Exception as e:

    print("Error", e)


if __name__=="__main__":
  main()