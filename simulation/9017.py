from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    ts = list(map(int, input().split()))
    counter = Counter(ts)
    scores = defaultdict(int)
    top4 = defaultdict(int)
    top5 = defaultdict(int)
    disqualify = set()
    for k, v in counter.items():
        if v < 6:
            disqualify.add(k)

    standings = []
    for i in range(n):
        standings.append((i+1, ts[i]))

    dq_cnt = 0
    for rank, team in standings:
        if team in disqualify:
            dq_cnt += 1
        else:
            if top4[team] < 4:
                scores[team] += (rank - dq_cnt)
                top4[team] += 1
            elif top4[team] == 4:
                top5[team] = (rank - dq_cnt)
                top4[team] += 1

    max_score = min(scores.values())
    champion = -1
    top5_score = float('inf')
    for t, score in scores.items():
        if score == max_score:
            if top5[t] < top5_score:
                champion = t
                top5_score = top5[t]

    print(champion)