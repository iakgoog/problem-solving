import math


def flippingMatrix(a):
    n = len(a) // 2
    m = 0
    total = 0
    for i in range(n):
        for j in range(n):
            m1 = max(a[i][j], a[2*n-i-1][j])
            m2 = max(a[i][2*n-j-1], a[2*n-i-1][2*n-j-1])
            total += max(m1, m2)
    return total

print(flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]))