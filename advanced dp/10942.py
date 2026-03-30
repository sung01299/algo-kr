'''
dp[i][j] = i~j 까지가 palindrome인지 1 or 0, i <= j
'''
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = 1

for i in range(1, n):
    if s[i-1] == s[i]:
        dp[i][i+1] = 1

for i in range(n-2, 0, -1):
    for j in range(i+2, n+1):
        if s[i-1] == s[j-1] and dp[i+1][j-1]:
            dp[i][j] = 1

t = int(input())
for _ in range(t):
    s, e = map(int, input().split())
    print(dp[s][e])