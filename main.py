import os
from xml.dom import minidom 
from Element import Element
from GetInputFromExcel import GeometeryFromExcel
import Functions 
import coordinates.SetNewKnoopCoordinates
from GetTablesFromXML import GetTablesFromXML 

def main():

	geometery_of_element = GeometeryFromExcel()

	# print geometery_of_element.length

	gebogen_element= Element(geometery_of_element.is_curved, geometery_of_element.length , geometery_of_element.height, geometery_of_element.radius, geometery_of_element.theta)
	print geometery_of_element.is_curved
	# some_coordinate = MiddleUpperCoordinates(gebogen_element)
	# print some_coordinate.new_y()

	xml_input_filename = "base_panel_1.xml"
	xml_parsed_root=GetXmlRoot(xml_input_filename)
	# knoop_table = DefineTables(xml_parsed_root)
	# support_node_table = DefineTables(xml_parsed_root)
	# support_line_table = DefineTables(xml_parsed_root)

	all_tables = GetTablesFromXML(xml_parsed_root)
	all_tables.get_tables()
	# knoop_table = all_tables.knoop_table
	# support_node_table = all_tables.support_node_table
	# support_line_table = all_tables.support_line_table


	knoop_objects = all_tables.knoop_table.getElementsByTagName("obj")
	support_node_objects = all_tables.support_node_table.getElementsByTagName("")
	# support_line_objects = support_line_table.getElementsByTagName("")
	coordinates.SetNewKnoopCoordinates.SubstituteNewCoordinates(knoop_objects,gebogen_element)

	
	write_to_file = True
	writeXML_to_File(xml_parsed_root,write_to_file)


# print straight_elemet.length
	
	
	
	# Coordinates = NewCoordinates(ImputSet)
	# print Coordinates
	 

	# KnoopTable = DefineTables(xml_parsed_root)
 
	# Knoop_objects = KnoopTable.getElementsByTagName("obj")

	# SetNewCoordinates(Coordinates,Knoop_objects)

	# writeXML_to_File(xml_parsed_root)




	# IsCurved=False

	# if IsCurved:
		
	# 	CurvedLength = 1500
	# 	Radius = 1000
	# 	print 'Curved length =', CurvedLength, ";", 'Radius=', Radius
	# 	GeometryParameters = IsCurved, CurvedLength, Radius
	# 	return GeometryParameters	
	# else:
	# 	Length = 3000
	# 	Height = 1200

	# 	print 'length=', Length, ";", 'Height=', Height
	# 	GeometryParameters = IsCurved, Length, Height
	# 	return
# def GetParameter():
	

def GetXmlRoot(filename):
	new_xml_name = str(filename)
	xml_parsed_root = minidom.parse(new_xml_name)
	return xml_parsed_root

def DefineTables(xml_parsed_root):
	Tables = xml_parsed_root.getElementsByTagName("table")

	for Table, item in enumerate(Tables, start=0):
		TableTrue = item.getAttribute('name')=='Node'
		if TableTrue:
		 	KnoopTableIndex = Table
		 	KnoopTable = Tables[KnoopTableIndex]
	return KnoopTable



# def NewCoordinates(GeometryParameters):
# 	IsCurved = GeometryParameters[0]
# 	if IsCurved:
# 		CurvedLength = GeometryParameters[1]
# 		Radius = GeometryParameters[2]

# 	else:
# 		Coordinates = StraightPannel(GeometryParameters)

# 	return Coordinates
# def StraightPannel(GeometryParameters):
# 	Length = GeometryParameters[1]
# 	Height = GeometryParameters[2]
	
# 	Coordinate_X2_new = Length/2
# 	Coordinate_X3_new = Length

# 	Coordinate_Y1_new = Height
# 	return Coordinate_X2_new, Coordinate_X3_new, Coordinate_Y1_new

# def SetNewCoordinates(Coordinates,Knoop_objects):
# 	Coordinate_X2_new = Coordinates[0]
# 	Coordinate_Y2_new = 0
# 	Coordinate_X3_new = Coordinates[1]
# 	Coordinate_Z1_new = Coordinates[2]

	
# 	Knoop_objects[2].getElementsByTagName("p1").item(0).setAttribute("v",str(Coordinate_X2_new)) #Set new coordinate for K3,X
# 	Knoop_objects[2].getElementsByTagName("p2").item(0).setAttribute("v",str(Coordinate_Y2_new)) #Set new coordinate for K3,X
# 	Knoop_objects[1].getElementsByTagName("p1").item(0).setAttribute("v",str(Coordinate_X3_new)) #Set new coordinate for K2,X
	
# 	Knoop_objects[3].getElementsByTagName("p1").item(0).setAttribute("v",str(Coordinate_X3_new)) #Set new coordinate for K4,X
# 	Knoop_objects[3].getElementsByTagName("p2").item(0).setAttribute("v",str(Coordinate_Y2_new)) #Set new coordinate for K4,Y
# 	Knoop_objects[3].getElementsByTagName("p3").item(0).setAttribute("v",str(Coordinate_Z1_new)) #Set new coordinate for K4,Z

# 	Knoop_objects[5].getElementsByTagName("p1").item(0).setAttribute("v",str(Coordinate_X2_new)) #Set new coordinate for K6,X
# 	Knoop_objects[5].getElementsByTagName("p2").item(0).setAttribute("v",str(Coordinate_Y2_new)) #Set new coordinate for K6,Y
# 	Knoop_objects[5].getElementsByTagName("p3").item(0).setAttribute("v",str(Coordinate_Z1_new)) #Set new coordinate for K6,Z

# 	Knoop_objects[4].getElementsByTagName("p3").item(0).setAttribute("v",str(Coordinate_Z1_new)) #Set new coordinate for K5,Z

# 	for K in Knoop_objects:
# 		K_X_coordinate = K.getElementsByTagName("p1").item(0)
# 		K_Y_coordinate = K.getElementsByTagName("p2").item(0)
# 		K_Z_coordinate = K.getElementsByTagName("p3").item(0)
# 		print K.getAttribute('nm') ,":", K_X_coordinate.getAttribute("v"), ":", K_Y_coordinate.getAttribute("v"), ":", K_Z_coordinate.getAttribute("v")

# def SetNewSupports():


#for Table in Tables:
#	 print Table.hasAttribute('name="Knoop"')
	
#KnoopTable = xml_parsed_root.getElementsByTagName("table").hasAtribute(name="Knoop")

	

#print Knoop_objects[1].getElementsByTagName("p1").item(0).getAttribute("v")
#print K.getAttribute('nm'), K_X_coordinate.getAttribute("v")



def writeXML_to_File(xml_root,write_to_file):
	if write_to_file:
		xml_printable = xml_root.toprettyxml()
		xmlEncoded = xml_printable.encode('utf-16')

		file_handler = open("filename.xml","wb")
		file_handler.write(xmlEncoded)
		file_handler.close()
		print "XML file updated"

if __name__ == "__main__" : 
	main()