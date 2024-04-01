class vehicle:
  def __init__(self, name, numTires):
    self.name = name
    self.numTires = numTires
    

class Car(vehicle):
  def __init__(self, worth, name, numTires):
    super().__init__(name, numTires)
    self.milage = worth

class Truck(vehicle):
  def __init__(self, name, numTires, milage):
    super().__init__(name, numTires)
    self.milage = milage

  def worth(self):
    return 50000 - (.25*self.milage)
    
class Bus(vehicle):
  def __init__(self, name, numTires, hometown):
    super().__init__(name, numTires)
    self.hometown = hometown

  def worth(self):
    return 50000