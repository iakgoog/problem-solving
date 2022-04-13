import functools

def miniMaxSum(arr):
    arr.sort()
    minSet = arr[0 : -1]
    maxSet = arr[1 : ]
    minVal = f"{functools.reduce(lambda a, b: a + b, minSet)}"
    maxVal = f"{functools.reduce(lambda a, b: a + b, maxSet)}"
    return f"{minVal} {maxVal}"


print(miniMaxSum([1, 3, 5, 7, 9]))