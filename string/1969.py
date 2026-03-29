from collections import defaultdict, Counter

cnt = defaultdict(list)

n, m = map(int, input().split())
for _ in range(n):
    s = str(input())
    for i, val in enumerate(s):
        cnt[i].append(val)

def get_most_freq(i):
    counter = Counter(cnt[i])
    most_freq = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[0]

    return most_freq[0], most_freq[1]

ans = ''
dist = 0

for i in range(m):
    c, count = get_most_freq(i)
    dist += n - count
    ans += c

print(ans)
print(dist)