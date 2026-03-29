from collections import Counter, defaultdict

n, k = map(int, input().split())
path = list(map(int, input().split()))

m = set()

def get_off(idx):
    res = 0
    max_nxt = -1
    for p in m:
        if p in path[idx:]:
            nxt_idx = path[idx:].index(p)
            if nxt_idx > max_nxt:
                max_nxt = nxt_idx
                res = p
        else:
            return p
    return res

ans = 0
for i, val in enumerate(path):
    m.add(val)
    if len(m) > n:
        off = get_off(i)
        m.remove(off)
        ans += 1
        m.add(val)

print(ans)