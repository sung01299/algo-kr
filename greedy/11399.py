n = int(input())
t = list(map(int, input().split()))

t.sort()

ans = 0
prev = 0
for i in range(n):
    ans += t[i] * (n-i)

print(ans)