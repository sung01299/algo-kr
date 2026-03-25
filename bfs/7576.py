from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(m):
    row = list(map(int, input().split()))
    board.append(row)

visited = [[False for _ in range(n)] for _ in range(m)]
dist = [[float('inf') for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
Q = deque()

for x in range(m):
    for y in range(n):
        if board[x][y] == 1:
            Q.append((x, y, 0))
            visited[x][y] = True
            dist[x][y] = 0
        if board[x][y] == 0:
            cnt += 1
if cnt != 0:
    while Q:
        cx, cy, cnt = Q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if (nx < 0 or nx >= m or ny < 0 or ny >= n): continue
            if (board[nx][ny] == -1 or visited[nx][ny]): continue

            Q.append((nx, ny, cnt + 1))
            dist[nx][ny] = min(dist[nx][ny], cnt + 1)
            visited[nx][ny] = True
    
    ans = -1
    for x in range(m):
        for y in range(n):
            if board[x][y] != -1:
                ans = max(ans, dist[x][y])
    print(-1 if ans == float('inf') else ans)
else:
    print(0)