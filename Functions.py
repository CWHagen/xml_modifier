import xlwings as xw
import os

def LoadExcelInputSheet():
	Excelname = 'Input_parameters'
	DirectoryPathName = os.path.dirname(os.path.realpath(__file__)) 	
	cwd = os.getcwd()
	ParameterWorkbook = xw.Book('Input_parameters.xlsx')
	OutputSheet = ParameterWorkbook.sheets['Excel_export']
	return OutputSheet