from audioop import reverse


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        if a + b < k:
            return 'NO'
    return 'YES'


print(twoArrays(10, [2, 1, 3], [7, 8, 9]))