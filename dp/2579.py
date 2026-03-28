'''
1 or 2 steps
no 3 stairs in a row
dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + score[i] -> move 2 steps
dp[i][2] = dp[i-1][1]  -> move 1 step
'''

n = int(input())
scores = [0]
for _ in range(n):
    scores.append(int(input()))

# i: (score, cnt)
dp = {}
dp[(0, 1)] = 0
dp[(0, 2)] = 0
dp[(1, 1)] = scores[1]
dp[(1, 2)] = scores[1]

for i in range(2, n+1):
    dp[(i, 2)] = dp[(i-1, 1)] + scores[i]
    if i > 1:
        dp[(i, 1)] = max(dp[(i-2, 1)], dp[(i-2, 2)]) + scores[i]

print(max(dp[(n,1)], dp[(n, 2)]))