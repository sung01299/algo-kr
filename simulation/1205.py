n, new_score, p = map(int, input().split())
if n > 0:
    scores = [-1 for _ in range(p)]
    scores_s = list(map(int, input().split()))
    for i in range(len(scores_s)):
        scores[i] = scores_s[i]

    added = False
    added_idx = 0
    for i in range(p):
        if new_score > scores[i]:
            scores.insert(i, new_score)
            added = True
            added_idx = i
            break

    if added:
        scores = scores[:p]
        ranks = [1]
        rank, cnt = 1, 0
        high_score = scores[0]
        for i in range(1, p):
            if scores[i] < high_score:
                rank += 1
                rank += cnt
                cnt = 0
                high_score = scores[i]
            else:
                cnt += 1
            ranks.append(rank)
        
        print(ranks[added_idx])

    else:
        print(-1)
else:
    print(1)