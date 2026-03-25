"""
time it takes to split iceberg into two or more
1. melt ice (토마토)
2. check if split (땅 몇개)
but how efficiently?
"""
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check_split(board, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if board[x][y] > 0 and not visited[x][y]:
                cnt += 1
                Q = deque()
                Q.append((x, y))
                visited[x][y] = True
                while Q:
                    cx, cy = Q.popleft()
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        if board[nx][ny] <= 0 or visited[nx][ny]: continue
                        Q.append((nx, ny))
                        visited[nx][ny] = True
    
    return cnt > 1

def melt_ice(board, n, m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0 and not visited[x][y]:
                Q = deque()
                Q.append((x, y))
                visited[x][y] = True
                while Q:
                    cx, cy = Q.popleft()
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                        if board[cx][cy] == 0 and board[nx][ny] > 0:
                            board[nx][ny] = max(board[nx][ny] - 1, 0)
                            if board[nx][ny] == 0:
                                visited[nx][ny] = True
                        if board[nx][ny] != 0 or visited[nx][ny]: continue

                        Q.append((nx, ny))
                        visited[nx][ny] = True
    
    return board

def empty(board):
    res = 0
    for row in board:
        res += sum(row)
    return res == 0



n, m = map(int, input().split())
board = []
for _ in range(n):
    row = [int(c) for c in input().split()]
    board.append(row)

cnt = 0
while not empty(board):
    melt_ice(board, n, m)
    cnt += 1
    split = check_split(board, n, m)
    if split:
        print(cnt)
        break

if empty(board): 
    print(0)

# print(melt_ice(board, n, m))
# print(check_split(board, n, m))
# print(melt_ice(board, n, m))
# print(check_split(board, n, m))

