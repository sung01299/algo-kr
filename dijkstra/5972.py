import heapq, sys
from collections import defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [float('inf') for _ in range(n+1)]

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, cur = heapq.heappop(heap)

        if distance[cur] < dist:
            continue

        for path in graph[cur]:
            if dist + path[1] < distance[path[0]]:
                distance[path[0]] = dist + path[1]
                heapq.heappush(heap, (dist + path[1], path[0]))

dijkstra(1)

print(distance[n] if distance[n] != float('inf') else 2147483647)