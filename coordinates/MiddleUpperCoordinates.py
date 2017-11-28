from Element import Element
import math
class MiddleUpperCoordinates:
	
	def __init__(self, element):
		self.element = element

	def new_x(self):
		if self.element.is_curved:
			return math.sin(self.element.theta/2)*self.element.radius
		else:
   			return self.element.length/2

   	def new_y(self):
	 	if self.element.is_curved:
			return self.element.radius - math.cos(self.element.theta/2)*self.element.radius
		else:
	   		return 0

   	def new_z(self):
 		return self.element.height


