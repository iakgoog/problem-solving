import math

def findMedian(arr):
    arr.sort()
    m = math.floor(len(arr) / 2)
    print(m)


print(findMedian([1, 2, 3, 4, 5]))