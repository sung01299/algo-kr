n = int(input())
arr = list(map(int, input().split()))
v = int(input())

cnt = 0
for elem in arr:
    if elem == v:
        cnt += 1

print(cnt)