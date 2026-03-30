'''
intuition 1: greedy?
dp
dp[i] = i를 제곱수의 합으로 표현할때 필요한 최소 갯수
dp[1] = 1, dp[2] = dp[1] + 1, dp[3] = dp[2] + 1, dp[4] = 1, dp[5] = dp[4] + 1

dp[i] = 1 if i in [제곱수] else min(dp[i-x], dp[i-y]) + 1
'''
n = int(input())
nums = set()
i = 1
while i * i <= n:
    nums.add(i*i)
    i += 1

# memory exceeded (knapsack dp)
# dp = [[float('inf') for _ in range(n+1)] for _ in range(len(nums) + 1)]
# for i in range(len(nums) + 1):
#     dp[i][0] = 0

# for i in range(1, len(nums) + 1):
#     for j in range(1, n+1):
#         if j == nums[i-1]:
#             dp[i][j] = 1
#         if i - 1 >= 0:
#             dp[i][j] = min(dp[i][j], dp[i-1][j])
#         if j - nums[i-1] >= 0:
#             dp[i][j] = min(dp[i][j], dp[i][j- nums[i-1]] + 1)

# # print(dp)
# print(dp[-1][-1])

dp = [float('inf') for _ in range(n+1)]

for i in range(1, n+1):
    if i in nums:
        dp[i] = 1
    else:
        for num in nums:
            if i - num >= 0:
                dp[i] = min(dp[i], dp[i-num] + 1)

print(dp[-1])