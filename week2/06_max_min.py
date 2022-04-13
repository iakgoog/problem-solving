import math
import sys

def maxMin(k, arr):
    arr.sort()
    l = len(arr)
    result = sys.maxsize
    for i in range(0, l - k + 1):
        n = i + k - 1
        result = min(result, arr[n] - arr[i])

    return result


print(maxMin(3, [100,200,300,350,400,401,402]))