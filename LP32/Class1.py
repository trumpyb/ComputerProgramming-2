
class Class1:
	def __init__(self, diameter):
		self.diameter = diameter
	
	def calcPrice(self):
		return 0.75 + 1.00 + .05*self.diameter*self.diameter
