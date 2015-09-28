import numpy as np

def census(populations, n, target):

  # Initializing a matrix with 0 to target columns and 0 to (n - 1) rows.
  # Columns represent all the different sums up to the target.
  # Rows represent the given array integers.

  matrix = np.array([[0 for x in range(target + 1)] for x in range(n)])


  # Initializes first column to 1; can always make a set whose sum = 0 with an empty set.
  for rowNum in range(n): 
    matrix[rowNum][0] = 1;

  for rowNum in range(n):
    for columnNum in range(target + 1):

      # The cell at row number rowNum nd column number columnNum is equal to the value of the cell at the row number above it.
      # If the above integer can already create a sum, any additional integers in the set won't change whether or not the new set can create the given sum.
      if matrix[rowNum - 1][columnNum] == 1:

        matrix[rowNum][columnNum] = 1

      # If the above cell is 0, it doesn't tell you anything about whether a new number will help create the sum.
      # Find a subset where that sum of the previous integers is a previous target (adding the given integer to the previous integers will hit the target)  
      elif matrix[rowNum - 1][columnNum - populations[rowNum]] == 1:

        matrix[rowNum][columnNum] = 1

      # There does not exist a subset of those integers that can create a target.
      else:

        matrix[rowNum][columnNum] = 0

  if (matrix[n-1][target] == 1): #1 if a subset exists that adds to the target.
    print('Yes, there is a subset of these areas where a total of exactly %d people live.' %(target))
  else:
    print('No, there does not exist a subset of these areas where a total of exactly %d people live.' %(target))

def main():
  # An array containing the populations of the 26 largest metro areas.
  
  populations = [12828837, 9461105, 6371773,
  5965343, 5946800, 5582170,
  5564635, 5268860, 4552402,
  4335391, 4296250, 4224851,
  4192887, 3439809, 3279833,
  3095313, 2812896, 2783243,
  2710489, 2543482, 2356285,
  2226009, 2149127, 2142508, 
  2134411]

  # Number of metro areas (26).
  metroAreas= len(populations)

  # The target value.
  target = 100000000

  # Testing w/ smaller numbers.
  '''
  populations = [1,2,4,5,9]
  metroAreas= len(populations)
  target = 15
  '''
  census(populations, metroAreas, target)

main()

