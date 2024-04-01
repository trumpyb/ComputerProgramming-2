from random import randint
import numpy as np

def maxMatrices(mat1, mat2):
  row = len(mat1)
  col = len(mat1[0])
  mout = np.empty((row, col), dtype = 'int') #[[0]*row]*col
  for x in range(row):
    for y in range(col):
      mout[x][y] = max(mat1[x][y], mat2[x][y])
  return mout


def printMatrix(mat):
  for row in mat:
    for num in row:
      print(f"{num:3d} ",end = "")
    print()
  pass




def main():
  mat1 = []
  mat2 = []

  for r in range(5):
    row1=[]
    row2=[]
    for c in range(5):
      rnd1 = randint(-50, 99)
      rnd2 = randint(-50, 99)
      row1.append(rnd1)
      row2.append(rnd2)
    mat1.append(row1)
    mat2.append(row2)

  print("Matrix 1: ")
  printMatrix(mat1)
  print("\nMatrix 2: ")
  printMatrix(mat2)
  matOut = maxMatrices(mat1, mat2)
  print("\nMax Matrix: ")
  printMatrix(matOut)

if __name__ == "__main__":
  main()