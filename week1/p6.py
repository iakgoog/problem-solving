def dectobin(d):
    if d > 1:
        return f"{dectobin(d // 2)}{d % 2}"
    else:
        return str(d)


def flippingBits(n):
    targetBin = dectobin(n)
    toFill = 32 - len(targetBin)
    targetBin = ('0' * toFill) + targetBin
    result = ''.join(list(map(lambda n: '1' if n == '0' else '0', list(targetBin))))
    return int(result, 2)

print(flippingBits(2147483647))