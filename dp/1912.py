import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(nums[0])
else:
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]

    ans = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        ans = max(ans, dp[i])

    print(ans)