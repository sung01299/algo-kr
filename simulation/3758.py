import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n, k, t, m = map(int, input().split())
    scores = [[0 for _ in range(k)] for _ in range(n)]
    submit = defaultdict(int)
    time = defaultdict(int)
    for i in range(m):
       team_id, q_num, s = map(int, input().split()) 
       scores[team_id - 1][q_num - 1] = max(s, scores[team_id - 1][q_num - 1])
       submit[team_id - 1] += 1
       time[team_id - 1] = i
    final_score = [sum(score) for score in scores]
    final_submit = [0 for _ in range(n)]
    for k, v in submit.items():
        final_submit[k] = v
    final_time = [0 for _ in range(n)]
    for k, v in time.items():
        final_time[k] = v
    rank = [i for i in range(n)]
    rank.sort(key=lambda x: (-final_score[x], final_submit[x], final_time[x]))
    print(rank.index(t-1) + 1)

t = int(input())
for _ in range(t):
    solve()