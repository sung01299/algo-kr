"""
https://www.acmicpc.net/problem/8979
"""

from collections import defaultdict

n, k = map(int, input().split())

scores = defaultdict(tuple)
for _ in range(n):
    nationality, g, s, b = map(int, input().split())
    scores[nationality] = (g, s, b)

sorted_scores = dict(sorted(scores.items(), key=lambda x: (x[1][0], x[1][1], x[1][2]), reverse=True))

rank = 1
rank_dict = defaultdict(int)
prev = list(sorted_scores.values())[0]
rank_dict[list(sorted_scores.keys())[0]] = rank

cnt = 1
for key, val in list(sorted_scores.items())[1:]:
    cnt += 1
    if val == prev:
        rank_dict[key] = rank
    else:
        rank_dict[key] = cnt
        rank = cnt
        prev = val

print(rank_dict[k])
