from Element import Element
import math
class EndUpperCoordinates:
	
	def __init__(self, element):
		self.element = element

	def new_x(self):
		if self.element.is_curved:
			return math.sin(self.element.theta)*self.element.radius
		else:
	   		return 0

   	def new_y(self):
   		return 0

   	def new_z(self):
   		return self.element.height


