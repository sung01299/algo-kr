import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = []
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

counter = Counter(words)
counter_key = list(counter.keys())

counter_key.sort(key= lambda x: (-counter[x], -len(x), x))

for v in counter_key:
    print(v)