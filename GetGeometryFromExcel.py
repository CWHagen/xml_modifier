import os
import pandas
import xlwings
from xlwings import Workbook, Sheet, Range, Chart
from GetInputFromExcel import GetInputFromExcel

class GetGeometryFromExcel:


	DirectoryPathName = os.path.dirname(os.path.realpath(__file__)) 	
	ExcelFileInput= str('\Input_parameters.xlsx')
	ExcelPathInput = DirectoryPathName + ExcelFileInput
	excelsheet_pandas_dataframe = pandas.read_excel(ExcelPathInput, sheetname='Input', col_index=0)
	
	# length=Range('I19').value
	# height=str(Excelsheet.ix[2]['Hoogte'])
	
	def __init__(self,excel_name):
		# super().__init__()
		self.excel_name = excel_name

	
	

data = GetGeometryFromExcel('Input_parameters')

print data.excelsheet_pandas_dataframe.lookup('Lengte', int(1))
# print data.excelsheet_pandas_dataframe.ix[2][1]
# print excelsheet_pandas_dataframe
