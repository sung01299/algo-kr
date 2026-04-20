'''
여행경로
DFS 
예외 처리 -> 중복 티켓 visited[idx]로 처리
'''

from collections import defaultdict
def solution(tickets):
    n = len(tickets)
    answer = []
    graph = defaultdict(list)
    visited = [False for _ in range(n)]
    idx = 0
    for s, e in tickets:
        graph[s].append((e, idx))
        idx += 1
        
    def backtracking(cur, path):
        if len(path) == n + 1:
            answer.append(path.copy())
            return
        
        for nxt, idx in graph[cur]:
            if not visited[idx]:
                path.append(nxt)
                visited[idx] = True
                backtracking(nxt, path)
                path.pop()
                visited[idx] = False
    
    backtracking("ICN", ["ICN"])
    answer.sort()
    
    return answer[0]