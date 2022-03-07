"""
Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
    # Write your code here
    total  = sum(arr)
    arr_min = arr[0]
    arr_max = arr[0]
    for number in arr:
        if number > arr_max:
            arr_max = number
        if number < arr_min:
            arr_min = number
    print(total - arr_max, total - arr_min)