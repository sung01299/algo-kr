from collections import deque

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    board = [[-1 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cabbages = []
    Q = deque()
    for _ in range(k):
        y, x = map(int, input().split())
        cabbages.append((x, y))
        board[x][y] = 1
    
    ans = 0
    for x, y in cabbages:
        if not visited[x][y]:
            ans += 1
            Q.append((x, y))
            visited[x][y] = True
            while Q:
                cx, cy = Q.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                    if board[nx][ny] == -1 or visited[nx][ny]: continue

                    Q.append((nx, ny))
                    visited[nx][ny] = True
    
    print(ans)