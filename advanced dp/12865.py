import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = []
v = []
for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j - w[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-w[i-1]] + v[i-1])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])