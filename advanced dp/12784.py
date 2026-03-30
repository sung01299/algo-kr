from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        graph[e].append((s, w))

    visited = [False for _ in range(n+1)]

    def f(start):
        visited[start] = True
        ans = 0
        for nxt in graph[start]:
            if not visited[nxt[0]]:
                ans += min(nxt[1], f(nxt[0]))
        
        return ans if ans else float('inf')

    res = f(1)
    print(res if res != float('inf') else 0)
