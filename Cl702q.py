class vehicle:
  def __init__(self, name, numTires):
    self.name = name
    self.numTires = numTires
    

class car(vehicle):
  def __init__(self, milage, name, numTires):
    super().__init__(name, numTires)
    self.milage = milage