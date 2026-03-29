n, m = map(int, input().split())

square = []
for _ in range(n):
    r = [int(c) for c in str(input())]
    square.append(r)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if square[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans*ans)