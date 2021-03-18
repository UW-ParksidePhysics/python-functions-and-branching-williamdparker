from matrix_solve import solve_equation, calculate_determinant

def main():
  matrices = [
    [[2., 5.], [4., 11.]],
    [[1., 2.], [3., 4.]]
  ]
  right_vectors = [
    [[2.],[-4.]],
    [[4.],[-2.]]
  ]
  for matrix, right_vector in zip(matrices, right_vectors):
    print(f'A = {matrix}')
    print(f'b = {right_vector}')
    solution = solve_equation(matrix, right_vector)
    print(f'det(A) = {calculate_determinant(matrix)}')
    print(f'x = {solution}') 
    print()

  print()
  return


if __name__ == '__main__':
  main()
