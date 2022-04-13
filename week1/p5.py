def lonelyinteger(a):
    count = {}
    for v in a:
        count[v] = count[v] + 1 if v in count else 1
    for k, v in count.items():
        if v == 1:
            return k


print(lonelyinteger([1,2,3,4,3,2,1]))