from collections import deque, defaultdict

n = int(input())
graph = []
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    row = []
    r = str(input())
    for c in r:
        row.append(int(c))
    graph.append(row)

rank = defaultdict(int)
num = 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True

    while Q:
        cx, cy = Q.popleft()
        rank[num] += 1
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1: continue
            if visited[nx][ny] or graph[nx][ny] == 0: continue
            Q.append((nx, ny))
            visited[nx][ny] = True
    return
    

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if not visited[i][j]:
                num += 1
                bfs(i, j)

print(len(rank))
rank = dict(sorted(rank.items()))
for v in rank.values():
    print(v)