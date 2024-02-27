class Shape:
  #Constructer sets up class data
  def __init__(self, length, width):
    self.length = length
    self.width = width 
    self._area = 0#self._ means private so it 
    self._perim = 0#should only be called in the class

  # Mutator/setters modifies class data
  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length): #Redundant
    self.length = length

  #Accesser/Getter returns class data
  def getArea(self):
    return self._area

  def getPerim(self):
    return self._perim


def main():
  len = int(input("Enter Length:"))
  wid = int(input("Enter Width:"))
  #Make a new Shape object
  shape = Shape(len, wid)
  # shape.setLength(5)
  shape.calculate()
  print("Area:",shape.getArea())
  print("Perimeter",shape.getPerim())
  pass


if __name__=="__main__":
  main()
