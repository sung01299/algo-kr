"""
https://www.acmicpc.net/problem/1157
"""

from collections import defaultdict
s = str(input())

hashmap = defaultdict(int)
for c in s:
    hashmap[c.upper()] += 1

max_count = max(hashmap.values())
max_freq = list(hashmap.values()).count(max_count)

if max_freq > 1:
    print("?")
else:
    print(max(hashmap, key=lambda x: hashmap[x]))

