"""Given a list of integers, count and return the number of times each value appears as an array of integers."""

def countingSort(arr):
    # Write your code here
    result = []
    for _ in range(100):
        result.append(0)
    for number in arr:
        result[number] += 1

    print(result)
    return result