"""Given a square matrix, calculate the absolute difference between the sums of its diagonals."""

def diagonalDifference(arr):
    # Write your code here
    #first diagonal sum
    n = len(arr)
    sum_1 = 0
    sum_2 = 0
    for i in range(n):
        sum_1 += arr[i][i]
    #second diagonal sum
    for i in range(n):
        sum_2 += arr[n-i-1][i]
    return abs(sum_1-sum_2)