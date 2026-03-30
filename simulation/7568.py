from collections import defaultdict

n = int(input())
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

s_p = list(sorted(p, key=lambda x: (x[0], x[1])))

hashmap = defaultdict(int)
m_weight, m_height = s_p[0][0], s_p[0][1]

for i in range(n):
    cnt = 0
    for j in range(i, n):
        if s_p[i][0] < s_p[j][0] and s_p[i][1] < s_p[j][1]:
            cnt += 1
    hashmap[s_p[i]] = cnt

ans = []
for v in p:
    ans.append(hashmap[v]+1)

print(*ans)