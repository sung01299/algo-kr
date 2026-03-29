doc = str(input())
search = str(input())

dp = [0 for _ in range(len(doc)+1)]

for i in range(len(doc) - len(search), -1, -1):
    if doc[i:i+len(search)] == search:
        dp[i] = max(dp[i], 1 + dp[i+len(search)])
    else:
        dp[i] = dp[i+1]

print(dp[0])