from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().rstrip()))

fvisited = [[False for _ in range(m)] for _ in range(n)]
fire = [[-1 for _ in range(m)] for _ in range(n)]

jvisited = [[False for _ in range(m)] for _ in range(n)]
j = [[-1 for _ in range(m)] for _ in range(n)]
jx, jy = 0, 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Q = deque()
for x in range(n):
    for y in range(m):
        if board[x][y] == "F":
            fire[x][y] = 0
            Q.append((x, y, 0))
            fvisited[x][y] = True
        if board[x][y] == "J":
            jx, jy = x, y
            j[x][y] = 0

# Fire
while Q:
    cx, cy, cnt = Q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if (nx < 0 or nx >= n or ny < 0 or ny >= m): continue
        if fire[nx][ny] >= 0 or board[nx][ny] == "#": continue

        fire[nx][ny] = fire[cx][cy] + 1
        Q.append((nx, ny, cnt+1))

# J
Q = deque()
Q.append((jx, jy, 0))
jvisited[jx][jy] = True
ans = float('inf')

while Q:
    cx, cy, cnt = Q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        # Escaped
        if (nx < 0 or nx >= n or ny < 0 or ny >= m):
            ans = min(ans, j[cx][cy] + 1)
            break
        if j[nx][ny] >= 0 or board[nx][ny] == "#": continue
        # Add constraint for fire
        if fire[nx][ny] != -1 and fire[nx][ny] <= j[cx][cy] + 1: continue

        j[nx][ny] = j[cx][cy] + 1
        Q.append((nx, ny, cnt + 1))

print("IMPOSSIBLE" if ans == float('inf') else ans)