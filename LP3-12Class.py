class ClLP312:
  def __init__(self, food, clothing, entertainment, rent):
    self.food = food
    self.clothing = clothing
    self.entertainment = entertainment
    self.rent = rent
    self._budget = 0
    self._percent = [0] * 4

  def __percent(self, number):
    return round((number/self._budget)*100,2)

  def calculate(self):
    self._budget = self.food + self.clothing + self.entertainment + self.rent
    self._percent[0] = self.__percent(self.food)
    self._percent[1] = self.__percent(self.clothing)
    self._percent[2] = self.__percent(self.entertainment)
    self._percent[3] = self.__percent(self.rent)

  def display(self):
    print("Catagory\t\tBudget")
    print(f"Food\t\t\t{self._percent[0]}%")
    print(f"Clothing\t\t{self._percent[1]}%")
    print(f"Entertainment\t{self._percent[2]}%")
    print(f"Rent\t\t\t{self._percent[3]}%")
    print()
    print(f"Total amount spent: ${self._budget:.2f}")
    

def main():
  food = float(input("How much did you spend on food?: $"))
  clth = float(input("How much did you spend on clothing?: $"))
  entn = float(input("How much did you spend on entertainment?: $"))
  rent = float(input("How much did you spend on rent?: $"))

  budget = ClLP312(food, clth, entn, rent)
  budget.calculate()
  budget.display()

  pass


if __name__=="__main__":
  main()
