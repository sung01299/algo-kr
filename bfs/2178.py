from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = [int(c) for c in input()]
    board.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
dist = [[float('inf') for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Q = deque()

# Starting point
Q.append((0, 0, 1))
visited[0][0] = True
dist[0][0] = 1

while Q:
    cx, cy, cnt = Q.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if (nx < 0 or nx >= n or ny < 0 or ny >= m): continue
        if (board[nx][ny] == 0 or visited[nx][ny]): continue
        Q.append((nx, ny, cnt + 1))
        visited[nx][ny] = True
        dist[nx][ny] = min(dist[nx][ny], cnt + 1)

print(dist[-1][-1])