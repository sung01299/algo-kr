"""
https://www.acmicpc.net/problem/2816
"""
k1, k2 = 0, 0
n = int(input())
for i in range(n):
    channel = str(input())
    if channel == "KBS1":
        k1 = i + 1
    if channel == "KBS2":
        k2 = i + 1

ans = ""
if k1 < k2:
    ans += "1" * (k1-1)
    ans += "4" * (k1-1)
    ans += "1" * (k2-1)
    ans += "4" * (k2-2)
else:
    ans += "1" * (k1-1)
    ans += "4" * (k1-1)
    ans += "1" * (k2)
    ans += "4" * (k2-1)

print(ans)