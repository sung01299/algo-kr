n, d = map(int, input().split())
shortcuts = []
for _ in range(n):
    s, e, l = map(int, input().split())
    shortcuts.append((s, e, l))

dp = [float('inf') for _ in range(d+1)]
dp[0] = 0

for end in range(1, d + 1):
    dp[end] = min(dp[end], dp[end-1] + 1)
    for shortcut in shortcuts:
        if end == shortcut[1]:
            dp[end] = min(dp[end], dp[shortcut[0]] + shortcut[2])

print(dp[-1])