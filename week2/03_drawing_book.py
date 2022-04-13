import math

def pageCount(n, p):
    mid = math.ceil(n / 2)
    gap = n - p
    if gap < mid:
        if gap == 1:
            if n % 2 == 0:
                return gap
            else:
                return 0
        return gap // 2
    else:
        return p // 2 

print(pageCount(5, 4))

# -1 23 45 6-