"""
x-1, x+1, 2*x
"""
from collections import deque

n, k = map(int, input().split())
limit = 100001
Q = deque()
visited = [False for _ in range(limit)]
Q.append((n, 0))
visited[n] = True
ans = float('inf')
while Q:
    cur, time = Q.popleft()
    if cur == k:
        ans = min(ans, time)

    
    nxt1 = cur - 1
    nxt2 = cur + 1
    nxt3 = 2 * cur

    if nxt3 >= 0 and nxt3 < limit and not visited[nxt3]:
        Q.append((nxt3, time))
        visited[nxt3] = True
    if nxt1 >= 0 and nxt1 < limit and not visited[nxt1]:
        Q.append((nxt1, time+1))
        visited[nxt1] = True
    if nxt2 >= 0 and nxt2 < limit and not visited[nxt2]:
        Q.append((nxt2, time+1))
        visited[nxt2] = True

print(ans)