from collections import defaultdict, deque

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False for _ in range(n + 1)]

Q = deque()
Q.append(1)
visited[1] = True

ans = 0
while Q:
    cur = Q.popleft()
    ans += 1
    for nxt in graph[cur]:
        if not visited[nxt]:
            Q.append(nxt)
            visited[nxt] = True

print(ans - 1)