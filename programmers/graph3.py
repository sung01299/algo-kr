'''
게임 맵 최단거리
BFS
'''

from collections import deque
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    Q = deque()
    Q.append((0, 0, 1))
    visited[0][0] = True
    while Q:
        cx, cy, cnt = Q.popleft()
        if cx == n - 1 and cy == m - 1:
            answer = cnt
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if maps[nx][ny] == 0 or visited[nx][ny]:
                continue
            Q.append((nx, ny, cnt + 1))
            visited[nx][ny] = True
            
    return answer