import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
board = []
for _ in range(m):
    r = list(map(int, input().split()))
    board.append(r)

memo = {}
def f(i, j):
    if i == 0 and j == 0:
        return 1

    if (i, j) in memo:
        return memo[(i, j)]
    
    memo[(i, j)] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if nx < 0 or nx > m-1 or ny < 0 or ny > n-1:
            continue
        if board[nx][ny] > board[i][j]:
            memo[(i, j)] += f(nx, ny)
    
    return memo[(i, j)]

print(f(m-1, n-1))