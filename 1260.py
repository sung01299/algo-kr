from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for k, val in graph.items():
    graph[k] = list(sorted(val, reverse=True))

dfs_visited = [False for _ in range(n+1)]
def dfs(graph, start):
    dfs_visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(graph, i)


for k, val in graph.items():
    graph[k] = list(sorted(val))

def bfs():
    bfs_path = []
    visited = [False for _ in range(n)]
    Q = deque()
    Q.append(v)
    visited[v-1] = True
    while Q:
        cur = Q.popleft()
        bfs_path.append(cur)
        for nxt in graph[cur]:
            if not visited[nxt-1]:
                Q.append(nxt)
                visited[nxt-1] = True
    return bfs_path

dfs(graph, v)
print()
print(*bfs())