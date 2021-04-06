#from matrix_solve import solve_equation, calculate_determinant

from array_matrix_solve import plot_solution
import numpy

def main():
  # matrices = [
  #   [[2., 5.], [4., 11.]],
  #   [[1., 2.], [3., 4.]]
  # ]
  # right_vectors = [
  #   [[2.],[-4.]],
  #   [[4.],[-2.]]
  # ]
  # for matrix, right_vector in zip(matrices, right_vectors):
  #   print(f'A = {matrix}')
  #   print(f'b = {right_vector}')
  #   solution = solve_equation(matrix, right_vector)
  #   print(f'det(A) = {calculate_determinant(matrix)}')
  #   print(f'x = {solution}') 
  #   print()

  # print()

  mat = numpy.array([[1,2],[4,5]])
  vector = numpy.array([[3],[6]])
  plot_solution(mat, vector)



if __name__ == '__main__':
  main()
