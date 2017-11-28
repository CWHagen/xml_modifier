import xlwings as xw
import os
import Functions

OutputSheet = LoadExcelInputSheet()


class GeometeryFromExcel:
	"""docstring for InputFromExcel"""
	def __init__(self):
		self.is_curved = OutputSheet.range('B1').value
		self.length = OutputSheet.range('B2').value
		self.hoogte = OutputSheet.range('B3').value
		self.radius = OutputSheet.range('B4').value
		self.theta = OutputSheet.range('B5').value

wb = InputFromExcel()

print wb.length


