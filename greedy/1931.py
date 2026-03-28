import sys
input = sys.stdin.readline

n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s, e))

times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = times[0][1]
for i in range(1, n):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]

print(cnt)