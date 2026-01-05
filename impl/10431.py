"""
https://www.acmicpc.net/problem/10431
"""

n = int(input())

for _ in range(n):
    tmp = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(tmp)-1):
        for j in range(i+1, len(tmp)):
            if tmp[i] > tmp[j]:
                tmp[i], tmp[j] = tmp[j], tmp[i]
                ans += 1

    print(tmp[0], ans)
