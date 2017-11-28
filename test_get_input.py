import os
import pandas
import xlwings
from xlwings import Workbook, Sheet, Range, Chart

DirectoryPathName = os.path.dirname(os.path.realpath(__file__)) 	
ExcelFileInput= str('\Input_parameters.xlsx')
ExcelPathInput = DirectoryPathName + ExcelFileInput
excelsheet_pandas_dataframe = pandas.read_excel(ExcelPathInput, sheetname='Input')
	
# length=Range('I19').value
height=str(excelsheet_pandas_dataframe.ix[2]['Hoogte'])

print height