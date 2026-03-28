import sys
input = sys.stdin.readline

n = int(input())

t = []
p = []

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(i + t[i], n+1):
        dp[i] = max(dp[i], dp[j] + p[i])

print(max(dp))