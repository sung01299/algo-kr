import sys
input = sys.stdin.readline

n = int(input())

lines = []
for _ in range(n):
    x, y = map(int, input().split())
    lines.append((x, y))

lines.sort(key=lambda x: (x[0], x[1]))

s, e = lines[0][0], lines[0][1]
ans = 0
for i in range(1, n):
    if lines[i][0] <= e:
        e = max(e, lines[i][1])
    else:
        ans += (e-s)
        s, e = lines[i][0], lines[i][1]

print(ans + e - s)