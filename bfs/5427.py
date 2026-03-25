from collections import deque

n = int(input())
for _ in range(n):
    w, h = map(int, input().split())
    board = []
    for _ in range(h):
        row = [c for c in input().rstrip()]
        board.append(row)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    fire = [[-1 for _ in range(w)] for _ in range(h)]
    sg = [[-1 for _ in range(w)] for _ in range(h)]
    Q1 = deque() # fire
    Q2 = deque() # sg

    for x in range(h):
        for y in range(w):
            if board[x][y] == '@':
                Q2.append((x, y, 0))
                sg[x][y] = 0
            if board[x][y] == '*':
                Q1.append((x, y, 0))
                fire[x][y] = 0

    # fire
    while Q1: 
        cx, cy, cnt = Q1.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if fire[nx][ny] >= 0 or board[nx][ny] == '#': continue
            Q1.append((nx, ny, cnt+1))
            fire[nx][ny] = fire[cx][cy] + 1

    # sg
    ans = float('inf')
    while Q2:
        cx, cy, cnt = Q2.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                ans = min(ans, sg[cx][cy] + 1)
                break
            if sg[nx][ny] >= 0 or board[nx][ny] == '#' or board[nx][ny] == '*': continue
            if fire[nx][ny] != -1 and fire[nx][ny] <= sg[cx][cy] + 1: continue
            
            Q2.append((nx, ny, cnt+1))
            sg[nx][ny] = sg[cx][cy] + 1

    print("IMPOSSIBLE" if ans == float('inf') else ans)