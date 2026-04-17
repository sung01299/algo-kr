'''
단어 변환
BFS
'''

from collections import defaultdict, deque
def compare(word1, word2):
    cnt = 0
    '''
    h:1, o: 1, t: 1 -> d: 1, o: 1, t: 1 => d: 1
    '''
    for a, b in zip(word1, word2):
        if a != b:
            cnt += 1
            if cnt > 1:
                return False
    return True

def solution(begin, target, words):
    n = len(words)
    answer = float('inf')
    graph = defaultdict(list)
    visited = defaultdict(bool)
    
    for i in range(n):
        if compare(begin, words[i]):
            graph[begin].append(words[i])
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if compare(words[i], words[j]):
                    graph[words[i]].append(words[j])
                    
    Q = deque()
    Q.append((begin, 0))
    visited[begin] = True
    while Q:
        cur, cnt = Q.popleft()
        if cur == target:
            answer = min(answer, cnt)
        
        for nxt in words:
            if compare(cur, nxt):
                if not visited[nxt]:
                    Q.append((nxt, cnt + 1))
                    visited[nxt] = True
    
    return answer if answer != float('inf') else 0