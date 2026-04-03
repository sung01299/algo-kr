from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

directions = [(1, -1), (1, 0), (1, 1)]
memo = [[[float('inf'), float('inf'), float('inf')] for _ in range(m)] for _ in range(n)]
for i in range(m):
    for d in range(3):
        memo[0][i][d] = board[0][i]

for i in range(1, n):
    for j in range(m):
        # direction 0
        px, py = i - 1, j + 1
        if px >= 0 and px <= n - 1 and py >= 0 and py <= m - 1:
            memo[i][j][0] = min(memo[i][j][0], min(memo[px][py][1], memo[px][py][2]) + board[i][j])
    
        # direction 1
        px, py = i - 1, j
        if px >= 0 and px <= n - 1 and py >= 0 and py <= m - 1:
            memo[i][j][1] = min(memo[i][j][1], min(memo[px][py][0], memo[px][py][2]) + board[i][j])

        # direction 2
        px, py = i - 1, j - 1
        if px >= 0 and px <= n - 1 and py >= 0 and py <= m - 1:
            memo[i][j][2] = min(memo[i][j][2], min(memo[px][py][0], memo[px][py][1]) + board[i][j])

ans = float('inf')
for i in range(m):
    ans = min(ans, min(memo[-1][i]))
print(ans)