n = int(input())

dp = [float('inf') for _ in range(n+1)]
path = [0 for _ in range(n+1)]
dp[1] = 0
path[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    path[i] = i-1

    if i % 2 == 0:
        if dp[i] >= dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2

    if i % 3 == 0:
        if dp[i] >= dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            path[i] = i // 3

cur = n
ans = []
print(dp[-1])
while True:
    ans.append(cur)
    if cur == 1:
        break
    cur = path[cur]

print(*ans)