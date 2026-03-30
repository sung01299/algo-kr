import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

nums = list(map(int, input().split()))
# print(graph)
visited = [False for _ in range(n)]
visited[0] = True

def f(i):
    visited[i] = True
    cost = nums[i]
    for nxt in graph[i]:
        if not visited[nxt]:
            cost = max(cost, cost + f(nxt))
    
    return cost if cost else float('-inf')

print(f(0))