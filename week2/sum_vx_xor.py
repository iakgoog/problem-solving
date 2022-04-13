import math

def sumXor(n):
    bi = bin(n).replace('0b', '')
    print(bi)
    count = 0
    for c in bi:
        if c == '0':
            count += 1
    if (n == 0):
        count = 0
    return pow(2, count)
    # while n > 0:
    #     t = n & 1
    #     if t == 0:
    #         c += 1
    #     n //= 2
    # return pow(2, c)


# print(str(sumXor(1000000000000000)))
print(str(sumXor(5)))