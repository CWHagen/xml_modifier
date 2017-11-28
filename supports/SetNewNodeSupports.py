from BeginLowerCoordinates import BeginLowerCoordinates
from MiddleLowerCoordinates import MiddleLowerCoordinates
from EndLowerCoordinates import EndLowerCoordinates
from EndUpperCoordinates import EndUpperCoordinates
from MiddleUpperCoordinates import MiddleUpperCoordinates
from BeginUpperCoordinates import BeginUpperCoordinates

# from Element import Element

def SubstituteNewNodeSupports(support_objects, element):

	begin_lower_coordinate = BeginLowerCoordinates(element)
	middle_lower_coordinate = MiddleLowerCoordinates(element)
	end_lower_coordinate = EndLowerCoordinates(element)

	end_upper_coordinates = EndUpperCoordinates(element)
	middle_upper_coordinate = MiddleUpperCoordinates(element)
	begin_upper_coordinate = BeginUpperCoordinates(element)

	# print middle_upper_coordinate.new_x(), middle_upper_coordinate.new_y(), middle_upper_coordinate.new_z()

	knoop_objects[0].getElementsByTagName("p1").item(0).setAttribute("v",str(begin_lower_coordinate.new_x())) #Set new coordinate for K1,X
	knoop_objects[0].getElementsByTagName("p2").item(0).setAttribute("v",str(begin_lower_coordinate.new_y())) #Set new coordinate for K1,Y
	knoop_objects[0].getElementsByTagName("p3").item(0).setAttribute("v",str(begin_lower_coordinate.new_z())) #Set new coordinate for K1,Z

	knoop_objects[2].getElementsByTagName("p1").item(0).setAttribute("v",str(middle_lower_coordinate.new_x())) #Set new coordinate for K3,X
	knoop_objects[2].getElementsByTagName("p2").item(0).setAttribute("v",str(middle_lower_coordinate.new_y())) #Set new coordinate for K3,Y
	knoop_objects[2].getElementsByTagName("p3").item(0).setAttribute("v",str(middle_lower_coordinate.new_z())) #Set new coordinate for K3,Z

	knoop_objects[1].getElementsByTagName("p1").item(0).setAttribute("v",str(end_lower_coordinate.new_x())) #Set new coordinate for K2,X
	knoop_objects[1].getElementsByTagName("p2").item(0).setAttribute("v",str(end_lower_coordinate.new_y())) #Set new coordinate for K2,Y
	knoop_objects[1].getElementsByTagName("p3").item(0).setAttribute("v",str(end_lower_coordinate.new_z())) #Set new coordinate for K2,Z

	knoop_objects[3].getElementsByTagName("p1").item(0).setAttribute("v",str(end_upper_coordinates.new_x())) #Set new coordinate for K4,X
	knoop_objects[3].getElementsByTagName("p2").item(0).setAttribute("v",str(end_upper_coordinates.new_y())) #Set new coordinate for K4,Y
	knoop_objects[3].getElementsByTagName("p3").item(0).setAttribute("v",str(end_upper_coordinates.new_z())) #Set new coordinate for K4,Z

	knoop_objects[5].getElementsByTagName("p1").item(0).setAttribute("v",str(middle_upper_coordinate.new_x())) #Set new coordinate for K6,X
	knoop_objects[5].getElementsByTagName("p2").item(0).setAttribute("v",str(middle_upper_coordinate.new_y())) #Set new coordinate for K6,Y
	knoop_objects[5].getElementsByTagName("p3").item(0).setAttribute("v",str(middle_upper_coordinate.new_z())) #Set new coordinate for K6,Z

	knoop_objects[4].getElementsByTagName("p1").item(0).setAttribute("v",str(begin_upper_coordinate.new_x())) #Set new coordinate for K5,Z
	knoop_objects[4].getElementsByTagName("p2").item(0).setAttribute("v",str(begin_upper_coordinate.new_y())) #Set new coordinate for K5,Z
	knoop_objects[4].getElementsByTagName("p3").item(0).setAttribute("v",str(begin_upper_coordinate.new_z())) #Set new coordinate for K5,Z