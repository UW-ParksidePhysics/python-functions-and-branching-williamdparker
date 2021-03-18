
# find inverse of any 2x2 matrix
#   input: matrix (nested list)
#   calculate determinant of the matrix
#   [[c, -b], [-d, a]] / determinant
#   output: inverse matrix (nested list)
def invert_matrix(matrix):
  determinant = calculate_determinant(matrix)
  inverse_matrix = []  # create empty list
  inverse_matrix.append([
    matrix[1][1],
    -matrix[0][1]
  ])
  inverse_matrix.append([
    -matrix[1][0],
    matrix[0][0]
  ])
  number_of_rows = len(matrix)
  number_of_columns = len(matrix[0])
  for i in range(number_of_rows):
    for j in range(number_of_columns):
      inverse_matrix[i][j] /= determinant
  return inverse_matrix


# calculate determinant of any 2x2 matrix
#   input: matrix (nested list)
#   matrix [[a, b], [c, d]]
#   output: a * d - b * c (float)
def calculate_determinant(matrix):
  determinant = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
  return determinant

# solve linear set of equations
#   a * x + b * y = f
#   c * x + d * y = g
#   [[x],[y]] = inverse_matrix * [[f],[g]]
#   input: matrix (nested list), right_vector (nested list)
#   output: solution_vector (nested list)
def solve_equation(matrix, right_vector):
  inverse_matrix = invert_matrix(matrix)
  solution_vector = [0., 0.]
  number_of_columns = len(inverse_matrix[0])
  number_of_rows = len(right_vector)
  for i in range(number_of_rows):
    for j in range(number_of_columns):
      solution_vector[i] += inverse_matrix[i][j]*right_vector[j][0]
  return solution_vector

