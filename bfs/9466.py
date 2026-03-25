from collections import defaultdict, deque

t = int(input())

for _ in range(t):
    n = int(input())
    hashmap = defaultdict(int)
    for idx, s in enumerate(list(map(int, input().split()))):
        hashmap[idx+1] = s
    visited = [False for _ in range(n)]
    Q = deque()
    ans = 0

    for start in range(1, n+1):
        if visited[start-1]:
            continue
        Q.append(start)
        visited[start-1] = True
        while Q:
            cur = Q.popleft()
            if hashmap[cur] == start:
                continue
            if visited[hashmap[cur] - 1]:
                ans += 1
                continue
            Q.append(hashmap[cur])
            visited[hashmap[cur] - 1] = True
        
    print(ans)