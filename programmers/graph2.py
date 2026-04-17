'''
네트워크
BFS
'''
from collections import defaultdict, deque
def solution(n, computers):
    answer = 0
    graph = defaultdict(list)
    for i in range(n):
        for idx, node in enumerate(computers[i]):
            if i != idx:
                if node == 1:
                    graph[i].append(idx)
    visited = [False for _ in range(n)]
    Q = deque()
    for i in range(n):
        if not visited[i]:
            answer += 1
            Q.append(i)
            visited[i] = True
            while Q:
                cur = Q.popleft()
                for nxt in graph[cur]:
                    if not visited[nxt]:
                        Q.append(nxt)
                        visited[nxt] = True
    return answer