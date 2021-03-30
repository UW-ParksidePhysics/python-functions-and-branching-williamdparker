# Main function: calculate_shape_properties 
#
# Calculate the area, perimeter, and diagonal length of a square
# given a side length
#
# Calculate the area, circumference, and diameter length of a circle
# given a radius
# 
from math import sqrt, pi
from sys import argv


def calculate_square_area(side_length):
  square_area = side_length * side_length
  return square_area


def calculate_square_perimeter(side_length):
  square_perimeter = 4 * side_length
  return square_perimeter


def calculate_square_diagonal_length(side_length):
  square_diagonal_length = sqrt(2) * side_length
  return square_diagonal_length


def calculate_circle_area(radius):
  circle_area = pi * radius**2
  return circle_area


def calculate_cirle_circumference(radius):
  circle_circumference = 2 * pi * radius
  return circle_circumference


def calculate_circle_diameter(radius):
  circle_diameter = 2 * radius
  return circle_diameter


def calculate_shape_properties(shape_type, principal_length):
  if shape_type == 'square':
    area = calculate_square_area(principal_length)
    perimeter = calculate_square_perimeter(principal_length)
    diagonal_length = calculate_square_diagonal_length(principal_length)

    shape_properties = (area, perimeter, diagonal_length)
  else:
    # circle calculations
    area = calculate_circle_area(principal_length)
    circumference = calculate_cirle_circumference(principal_length)
    diameter = calculate_circle_diameter(principal_length)

    shape_properties = (area, circumference, diameter)

  return shape_properties


# Ask user for shape type and length
# type_of_shape = input("Which shape do you want?  ")
# length = float(input("What is the principal length of that shape?  "))

# Read in shape type and length from command-line arguments
# argc = len(argv)
# type_of_shape = argv[1]
# length = float(argv[2])

# Read in shape type and length from file (shape.txt)
file_array = open('shape.txt', 'r')
file_contents = file_array.readlines()
file_array.close()

output_file = open('shape_properties.txt','w')

for line in file_contents:
  elements = line.split() 
  type_of_shape = elements[0]
  length = float(elements[1])
  area, boundary_length, cross_length = calculate_shape_properties(type_of_shape, length)
  output_string = f"{type_of_shape}: Length {length}, Area {area},"
  output_string += f" Boundary {boundary_length}, Cross Length {cross_length}\n"
  output_file.write(output_string)
  
output_file.close()
