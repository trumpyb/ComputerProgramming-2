class Circle:
  def __init__(self, radius):
    self.radius = radius
    self._area = 0
    self._perim = 0

  def calc(self):
    self._area = 3.14159 * self.radius ** 2
    self._perim = 3.14159 * self.radius * 2

  def getArea(self):
    return self._area

  def getPerim(self):
    return self._perim


radius = float(input("Enter Radius: "))

circle = Circle(radius)
circle.calc()

print("Area:",circle.getArea())
print("Perimeter",circle.getPerim())