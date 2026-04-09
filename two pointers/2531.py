from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

for i in range(n-1):
    sushi.append(sushi[i])

s = defaultdict(int)
for i in range(k):
    s[sushi[i]] += 1
ans = len(s.keys()) + 1 if c not in s else len(s.keys())

for i in range(k, len(sushi)):
    s[sushi[i-k]] -= 1
    if s[sushi[i-k]] == 0:
        del s[sushi[i-k]]
    s[sushi[i]] += 1
    ans = max(ans, len(s.keys()) + 1 if c not in s else len(s.keys()))

print(ans)