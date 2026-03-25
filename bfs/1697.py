"""
x-1, x+1 or 2*x
"""
from collections import deque

n, k = map(int, input().split())

limit = 100001
Q  = deque()
visited = [False for _ in range(limit)]

Q.append((n, 0))
visited[n] = True

ans = float('inf')
while Q:
    cur, t = Q.popleft()
    if cur == k:
        ans = min(ans, t)

    for new in [cur - 1, cur + 1, cur * 2]:
        if new >= 0 and new < limit and not visited[new]:
            Q.append((new, t + 1))
            visited[new] = True

print(ans)