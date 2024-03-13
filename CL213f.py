class Cl213f:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0

  def calc(self):
    if self.kwh < 2000:
      self.cost = self.kwh * .07
    elif 2000 < self.kwh < 10000:
      self.cost = (2000 * .07) + ((self.kwh-2000)*.05)

    elif self.kwh > 10000:
      self.cost = (2000 * .07) + (8000 * .05) + ((self.kwh-10000)*.04)

    self.cost = round(self.cost, 2)
      
  def __str__(self):
    return f"Cost of {self.kwh} is {self.cost}"