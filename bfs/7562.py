from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    Q = deque()
    Q.append((startx, starty, 0))
    visited[startx][starty] = True

    while Q:
        cx, cy, cnt = Q.popleft()
        if cx == endx and cy == endy:
            print(cnt)
            break
        for dx, dy in [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (2, -1), (1, -2)]:
            nx = cx + dx
            ny = cy + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[nx][ny]: continue

            Q.append((nx, ny, cnt + 1))
            visited[nx][ny] = True