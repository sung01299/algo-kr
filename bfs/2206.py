from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = [int(c) for c in input().rstrip()]
    board.append(row)
# use super, not use
visited = [[[False, False] for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque()
Q.append((0, 0, 0, 1))
visited[0][0][0] = True
ans = float('inf')
while Q:
    cx, cy, sp, cnt = Q.popleft()
    if cx == n-1 and cy == m-1:
        ans = min(ans, cnt)
        break
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        
        if board[nx][ny] == 1 and sp == 0:
            visited[nx][ny][1] = visited[cx][cy][0] + 1
            Q.append((nx, ny, sp+1, cnt + 1))
        elif board[nx][ny] == 0 and not visited[nx][ny][sp]:
            visited[nx][ny][sp] = visited[cx][cy][sp] + 1
            Q.append((nx, ny, sp, cnt + 1))

print(-1 if ans == float('inf') else ans)     