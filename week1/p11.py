def birthday(s, d, m):
    t_sum = sum(s[:m])
    count = 0
    if len(s) == 1 and s[0] == d or t_sum == d:
        count += 1
    for i in range(len(s) - m):
        t_sum += s[i + m] - s[i]    
        if t_sum == d:
            count += 1
    return count


arr = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
# 22, 25, 
d = 18
m = 7

print(birthday(arr, d, m))


# def maxSum(arr, n, k):
#     max_sum = 0

#     for i in range(n - k + 1):
#         current_sum = 0
#         for j in range(k):
#             current_sum = current_sum + arr[i + j]

#         max_sum = max(current_sum, max_sum)

#     return max_sum

# def maxSum(arr, n, k):
#     if n < k:
#         print('Invalid')
#         return -1

#     window_sum = sum(arr[:k])
#     max_sum = window_sum

#     for i in range(n - k):
#         window_sum = window_sum - arr[i] + arr[i + k]
#         max_sum = max(window_sum, max_sum)

#     return max_sum


# arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# k = 4
# n = len(arr)

# print(maxSum(arr, n, k))