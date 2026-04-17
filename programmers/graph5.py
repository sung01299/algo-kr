'''
아이템 줍기
BFS
예외 처리 -> 좌표 2배 처리
'''

from collections import deque
def is_border(x, y, graph):
    if graph[x-1][y] == 0 or graph[x+1][y] == 0 or graph[x][y-1] == 0 or graph[x][y+1] == 0:
        return True
    if graph[x+1][y+1] == 0 or graph[x+1][y-1] == 0 or graph[x-1][y+1] == 0 or graph[x-1][y-1] == 0:
        return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = float('inf')
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    graph = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(102)] for _ in range(102)]
    
    for r in rectangle:
        sx, sy, ex, ey = r
        # 박스 채우기
        for i in range(sx*2, ex*2 + 1):
            for j in range(sy*2, ey*2 + 1):
                graph[i][j] = 1

    # 1, 3 -> 6, 1
    # 7, 8 -> 1, 7
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    Q = deque()
    Q.append((characterX, characterY, 0))
    visited[characterX][characterY] = True
    while Q:
        cx, cy, cnt = Q.popleft()
        if cx == itemX and cy == itemY:
            answer = min(answer, cnt)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if graph[nx][ny] == 0 or visited[nx][ny] or not is_border(nx, ny, graph): continue
            Q.append((nx, ny, cnt+1))
            visited[nx][ny] = True
    
    return answer // 2