from collections import deque

k = int(input())
w, h = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

# left 0, left 1, left 2(k)
# [0, 0, 0]
visited = [[[False for _ in range(k+1)] for _ in range(w)] for _ in range(h)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
smove = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

Q = deque()
Q.append((0, 0, k, 0))
visited[0][0][k] = True
ans = float('inf')

while Q:
    cx, cy, mp, cnt = Q.popleft()
    if cx == h-1 and cy == w-1:
        print(cnt)
        break
    if mp > 0:
        for sdx, sdy in smove:
            nx = cx + sdx
            ny = cy + sdy
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if board[nx][ny] == 1: continue
            if board[nx][ny] == 0 and not visited[nx][ny][mp-1]:
                Q.append((nx, ny, mp-1, cnt+1))
                visited[nx][ny][mp-1] = True

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
        if board[nx][ny] == 1 or visited[nx][ny][mp]: continue
        Q.append((nx, ny, mp, cnt+1))
        visited[nx][ny][mp] = True
            
else:
    print(-1)