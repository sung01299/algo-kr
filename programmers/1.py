'''
혼자 놀기의 달인
DFS
'''

def solution(cards):
    n = len(cards)
    visited = [False for _ in range(n)]
    groups = []
    
    for i in range(n):
        if not visited[i]:
            group = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                group.append(cur)
                cur = cards[cur] - 1
            groups.append(len(group))
    
    groups.sort(reverse=True)
    
    return 0 if len(groups) <= 1 else groups[0] * groups[1]