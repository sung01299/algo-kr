import sys
sys.setrecursionlimit(10**6)

n = int(input())

dp = {}
dp[1] = 0

# def f(i):
#     if i == 1:
#         return 0

#     if i in dp:
#         return dp[i]
    
#     dp[i] = 1 + f(i-1)

#     if i % 3 == 0:
#         dp[i] = min(dp[i], 1 + f(i // 3))

#     if i % 2 == 0:
#         dp[i] = min(dp[i], 1 + f(i // 2))

#     return dp[i]
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)


print(dp[n])