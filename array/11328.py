from collections import Counter

n = int(input())

for _ in range(n):
    a, b = map(str, input().split())
    if Counter(a) == Counter(b):
        print("Possible")
    else:
        print("Impossible")