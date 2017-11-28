from Element import Element
import math
class EndLowerCoordinates:
	
	def __init__(self, element):
		self.element = element

	def new_x(self):
		if self.element.is_curved:
			return math.sin(self.element.theta)*self.element.radius
		else:
	   		return self.element.length

   	def new_y(self):
   		return 0

   	def new_z(self):
   		return 0


