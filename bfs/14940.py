from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

table = [[-1 for _ in range(m)] for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            table[i][j] = 0
            x, y = i, j
        elif board[i][j] == 0:
            table[i][j] = 0
        else:
            table[i][j] = float('inf')

visited = [[False for _ in range(m)] for _ in range(n)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

Q = deque()
Q.append((x, y, 0))
visited[x][y] = True

while Q:
    cx, cy, cnt = Q.popleft()
    table[cx][cy] = min(table[cx][cy], cnt)
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1: continue
        if board[nx][ny] == 0 or visited[nx][ny]: continue
        Q.append((nx, ny, cnt+1))
        visited[nx][ny] = True

for i in range(n):
    for j in range(m):
        if table[i][j] == float('inf'):
            table[i][j] = -1

for row in table:
    print(*row)