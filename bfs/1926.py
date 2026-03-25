from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

num = 0
mx = 0

# visited, dx, dy, Queue
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Q = deque()

for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and not visited[x][y]:
            num += 1
            # Add starting point, mark visited
            Q.append((x, y))
            visited[x][y] = True

            area = 0
            # One cycle
            while Q:
                area += 1
                # Pop from Queue, Add adjacent points
                cx, cy = Q.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    # check boundaries, visited, valid step
                    if (nx < 0 or nx >= n or ny < 0 or ny >= m): continue
                    if board[nx][ny] != 1 or visited[nx][ny]: continue
                    # Mark visited, append new points
                    visited[nx][ny] = True
                    Q.append((nx, ny))
            
            mx = max(mx, area)

print(num)
print(mx)