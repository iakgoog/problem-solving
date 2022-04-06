def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    l = len(arr)
    for i in range(l):
        sum1 += arr[i][i]
        sum2 += arr[l - 1 - i][i]
    return abs(sum1 - sum2)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))