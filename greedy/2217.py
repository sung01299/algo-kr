n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

ans = 0
for i in range(n):
    ans = max(ans, ropes[i] * (n-i))

print(ans)