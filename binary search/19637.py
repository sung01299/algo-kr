import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names = []
conditions = []
for _ in range(n):
    name, cond = map(str, input().split())
    if len(conditions) > 0:
        if int(cond) != conditions[-1]:
            names.append(name)
            conditions.append(int(cond))
    else:
        names.append(name)
        conditions.append(int(cond))

def bin_search(val):
    l, r = 0, len(conditions)
    while l < r:
        mid = l + (r - l) // 2
        if conditions[mid] < val:
            l = mid + 1
        else:
            r = mid
    return l

for _ in range(m):
    res = bin_search(int(input()))
    print(names[res])