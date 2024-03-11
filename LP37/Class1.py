
class Class1:
	def __init__(self, num1, num2):
		self.num1 = float(num1)
		self.num2 = float(num2)
		
	def calculate(self):
		output = [self.num1/self.num2, self.num1%self.num2, self.num2/self.num1, self.num2%self.num1]
		return output
