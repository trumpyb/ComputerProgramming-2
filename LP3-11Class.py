class ClLP312:
  def __init__(self, designing, coding, debugging, testing):
    self.designing = designing
    self.coding = coding
    self.debugging = debugging
    self.testing = testing
    self._budget = 0
    self._percent = [0] * 4

  def __percent(self, number):
    return round((number/self._budget)*100,2)

  def calculate(self):
    self._budget = self.designing + self.coding + self.debugging + self.testing
    self._percent[0] = self.__percent(self.designing)
    self._percent[1] = self.__percent(self.coding)
    self._percent[2] = self.__percent(self.debugging)
    self._percent[3] = self.__percent(self.testing)

  def display(self):
    print("Catagory\t\tBudget")
    print(f"designing\t\t\t{self._percent[0]}%")
    print(f"coding\t\t{self._percent[1]}%")
    print(f"debugging\t{self._percent[2]}%")
    print(f"testing\t\t\t{self._percent[3]}%")
    print()
    print(f"Total amount of time spent: {self._budget:.2f}")


def main():
  designing = float(input("How much time did you spend on designing?: "))
  code= float(input("How much time did you spend on coding?: "))
  debug= float(input("How much time did you spend on debugging?: "))
  testing = float(input("How much time did you spend on testing?: "))

  budget = ClLP312(designing, code, debug, testing)
  budget.calculate()
  budget.display()

  pass


if __name__=="__main__":
  main()


