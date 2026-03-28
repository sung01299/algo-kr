import sys
input = sys.stdin.readline

n = int(input())
triangle = [[] for _ in range(n)]
dp = [[] for _ in range(n)]
for i in range(n):
    r = list(map(int, input().split()))
    triangle[i] = r

if n >= 1:
    dp[0] = [triangle[0][0]]
if n >= 2:
    dp[1].append(triangle[0][0] + triangle[1][0])
    dp[1].append(triangle[0][0] + triangle[1][1])
if n >= 3:
    for lvl in range(2, n):
        for i in range(lvl + 1):
            if i == 0:
                dp[lvl].append(dp[lvl-1][i] + triangle[lvl][i])
            elif i == lvl:
                dp[lvl].append(dp[lvl-1][lvl-1] + triangle[lvl][i])
            else:
                dp[lvl].append(max(dp[lvl-1][i-1], dp[lvl-1][i]) + triangle[lvl][i])

print(max(dp[-1]))
