import math

n, k = map(int, input().split())

boy = [0 for _ in range(6)]
girl = [0 for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    if s == 1:
        boy[y - 1] += 1
    else:
        girl[y - 1] += 1

cnt = 0
for y in boy:
    cnt += (math.ceil(y / k))
for y in girl:
    cnt += (math.ceil(y / k))

print(cnt)