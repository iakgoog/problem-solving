def sockMerchant(n, ar):
    d = {}
    p = 0
    for v in ar:
        if v in d:
            d[v] += 1
            if d[v] == 2:
                d[v] = 0
                p += 1
        else:
            d[v] = 1
    return p



print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))