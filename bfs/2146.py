"""
1. identify different continents
2. find boundaries
3. calculate shortest path
"""
from collections import deque, defaultdict

boundaries = defaultdict(list)

n = int(input())
board = []
for _ in range(n):
    row = [-1 if int(c) == 1 else 0 for c in input().split()]
    board.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

continent = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        Q = deque()
        if board[x][y] == -1 and not visited[x][y]:
            continent += 1
            Q.append((x, y))
            board[x][y] = continent
            visited[x][y] = True
            while Q:
                cx, cy = Q.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                    if board[nx][ny] == 0:
                        if (cx, cy) not in boundaries[continent]:
                            boundaries[continent].append((cx, cy))
                    if board[nx][ny] == 0 or visited[nx][ny]: continue

                    Q.append((nx, ny))
                    visited[nx][ny] = True
                    board[nx][ny] = continent

def bfs(x, y, con):
    visited = [[False for _ in range(n)] for _ in range(n)]
    Q = deque()
    Q.append((x, y, 0))
    visited[x][y] = True
    ans = float('inf')
    while Q:
        cx, cy, cnt = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if board[nx][ny] != 0 and board[nx][ny] != con:
                ans = min(ans, cnt)
                break
            if board[nx][ny] != 0 or visited[nx][ny]: continue
            Q.append((nx, ny, cnt+1))
            visited[nx][ny] = True
    
    return ans

ans = float('inf')
for con in range(1, continent+1):
    b = boundaries[con]
    for x, y in b:
        ans = min(ans, bfs(x, y, con))

print(ans)