class vehicle:
  def __init__(self, name, numTires):
    self.name = name
    self.numTires = numTires
    

class Car(vehicle):
  def __init__(self, worth, name, numTires):
    super().__init__(name, numTires)
    self.worth = worth

class Truck(vehicle):
  def __init__(self, name, numTires, milage):
    super().__init__(name, numTires)
    self.milage = milage
    self.worth = 50000 - (.25*self.milage) 

  def __str__(self):
    return f"{self.name}, {self.worth}"
    
class Bus(vehicle):
  def __init__(self, name, numTires, hometown):
    super().__init__(name, numTires)
    self.hometown = hometown
    self.worth = 50000