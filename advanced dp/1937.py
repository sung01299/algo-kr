import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(n+2)]]
for _ in range(n):
    row = [0]
    r = list(map(int, input().split()))
    for c in r:
        row.append(c)
    row.append(0)
    board.append(row)
board.append([0 for _ in range(n+2)])

memo = {}
def f(i, j):
    if i == 0 or i == n+1 or j == 0 or j == n+1:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]
    
    memo[(i, j)] = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if board[nx][ny] > board[i][j]:
            memo[(i, j)] = max(memo[(i, j)], f(nx, ny) + 1)
            
    return memo[(i, j)]

ans = 0
for i in range(1, n+2):
    for j in range(1, n+2):
        ans = max(ans, f(i, j))

print(ans)