import sys
input = sys.stdin.readline

n = int(input())

t = [0]
p = [0]

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

future = {}
dp = [0 for _ in range(n+1)]

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + t[i] - 1
    if fin_date <= n:
        dp[fin_date] = max(dp[fin_date], dp[i-1] + p[i])

print(max(dp))