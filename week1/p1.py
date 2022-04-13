# function plusMinus(arr) {
#     // Write your code here
#     const counts = {
#         zero: 0,
#         positive: 0,
#         negative: 0
#     };
#     for (const num of arr) {
#         if (num === 0) counts.zero += 1
#         if (num > 0) counts.positive += 1
#         if (num < 0) counts.negative +=1
#     }
#     console.log(financial(counts.positive / arr.length))
#     console.log(financial(counts.negative / arr.length))
#     console.log(financial(counts.zero / arr.length))
# }



def plusMinus(arr):
    zero = 0
    pos = 0
    neg = 0
    for num in arr:
        if num == 0:
            zero += 1
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
    l = len(arr)
    print(round(pos / l, 6))
    print(round(neg / l, 6))
    print(round(zero / l, 6))


plusMinus([1, 1, 0, -1, -1])