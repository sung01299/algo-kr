"""
RG, B
R, G, B
"""
from collections import deque

N = int(input())
board1 = []
board2 = []
for _ in range(N):
    row = [c for c in input()]
    row2 = ["R" if c == "G" else c for c in row]
    board1.append(row)
    board2.append(row2)
visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q1 = deque()
ans = 0
for x in range(N):
    for y in range(N):
        if not visited1[x][y]:
            Q1.append((x, y))
            visited1[x][y] = True
            ans += 1
            while Q1:
                cx, cy = Q1.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if board1[nx][ny] != board1[cx][cy] or visited1[nx][ny]: continue

                    Q1.append((nx, ny))
                    visited1[nx][ny] = True

Q2 = deque()
ans2 = 0
for x in range(N):
    for y in range(N):
        if not visited2[x][y]:
            Q2.append((x, y))
            visited2[x][y] = True
            ans2 += 1
            while Q2:
                cx, cy = Q2.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if board2[nx][ny] != board2[cx][cy] or visited2[nx][ny]: continue

                    Q2.append((nx, ny))
                    visited2[nx][ny] = True

print(ans, ans2)
