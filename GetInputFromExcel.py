import xlwings as xw
import os
from Functions import LoadExcelInputSheet

OutputSheet = LoadExcelInputSheet()


class GeometeryFromExcel:
	"""docstring for InputFromExcel"""
	def __init__(self):
		self.is_curved = OutputSheet.range('B1').value == "Ja"
		self.length = OutputSheet.range('B2').value
		self.height = OutputSheet.range('B3').value
		self.radius = OutputSheet.range('B4').value
		self.theta = OutputSheet.range('B5').value

# wb = GeometeryFromExcel()
# print wb.length

class NodeSupportsFromExcel:
	"""docstring for NodeSupportsFromExcel"""
	def __init__(self):
		self.LeftLowerNode = [int(OutputSheet.range('B9').value) , \
							int(OutputSheet.range('C9').value) , \
							int(OutputSheet.range('D9').value ), \
							int(OutputSheet.range('E9').value ), \
							int(OutputSheet.range('F9').value ), \
							int(OutputSheet.range('G9').value ), \
							 ]
		self.RightLowerNode = [int(OutputSheet.range('B10').value) , \
							int(OutputSheet.range('C10').value) , \
							int(OutputSheet.range('D10').value ), \
							int(OutputSheet.range('E10').value ), \
							int(OutputSheet.range('F10').value ), \
							int(OutputSheet.range('G10').value ), \
							 ]
		self.RightUpperNode = [int(OutputSheet.range('B11').value) , \
							int(OutputSheet.range('C11').value) , \
							int(OutputSheet.range('D11').value ), \
							int(OutputSheet.range('E11').value ), \
							int(OutputSheet.range('F11').value ), \
							int(OutputSheet.range('G11').value ), \
							 ]
		self.LeftUpperNode = [int(OutputSheet.range('B12').value) , \
							int(OutputSheet.range('C12').value) , \
							int(OutputSheet.range('D12').value ), \
							int(OutputSheet.range('E12').value ), \
							int(OutputSheet.range('F12').value ), \
							int(OutputSheet.range('G12').value ), \
							 ]							 


# wb = NodeSupportsFromExcel()
# print wb.LeftLowerNode
		
