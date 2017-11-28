import Element
class CurvedElement(Element):
	def __init__(self, lengh, height, radius):
		super().__init__(lengh, height)
		self.radius = radius