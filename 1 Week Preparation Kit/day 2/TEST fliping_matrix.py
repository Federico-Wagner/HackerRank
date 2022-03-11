"""
Sean invented a game involving a matrix where each cell of the matrix contains an integer. He
can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum
of the elements in the submatrix located in the upper-left quadrant of the matrix.
Given the initial configurations for matrices, help Sean reverse the rows and columns of each matrix in the
best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

"""

def flippingMatrix(matrix):
 # Write your code here
 n = len(matrix)
 m= n -1
 partial_result = []
 for i in range(n // 2):
 for j in range(n // 2):
 foursomes = [matrix[i][j], matrix[i][m-j], matrix[m-i][j],
matrix[m-i][m-j]]
 partial_result.append(max(foursomes))
 return sum(partial_result)
