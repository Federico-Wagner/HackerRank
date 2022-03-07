"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal."""

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    for number in arr:
        if number > 0:
            positive +=1
        elif number <0:
            negative +=1
        else:
            zeros +=1
    print(positive/len(arr))
    print(negative/len(arr))
    print(zeros/len(arr))