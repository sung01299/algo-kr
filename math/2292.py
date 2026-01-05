"""
https://www.acmicpc.net/problem/2292
"""

n = int(input())

if n == 1:
    print(1)
else:
    cnt = 1
    n -= 1
    while n > 0:
        n -= (6 * cnt)
        cnt += 1
        if n <= 0:
            break
    print(cnt)