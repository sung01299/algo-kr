h, w = map(int, input().split())
rain = list(map(int, input().split()))

ans = 0
for i in range(1, len(rain)-1):
    l_max, r_max = max(rain[:i]), max(rain[i+1:])
    add = min(l_max, r_max) - rain[i]
    if add > 0:
        ans += add

print(ans)