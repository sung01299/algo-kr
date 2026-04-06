n = int(input())

heights = [0 for _ in range(1001)]
max_height = 0
max_height_idx = 0

for _ in range(n):
    l, h = map(int, input().split())
    if h > max_height:
        max_height = h
        max_height_idx = l
    heights[l] = h

cur = 0
ans = 0
for i in range(max_height_idx+1):
    cur = max(cur, heights[i])
    ans += cur

cur = 0
for i in range(1000, max_height_idx, -1):
    cur = max(cur, heights[i])
    ans += cur

print(ans)