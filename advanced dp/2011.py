'''
dp[i] = i에서 시작하는 갯수
if s[i]가 한 자리수 가능하면 (1-9 사이, i+1가 0이 아님)
dp[i] += f(i+1)
if s[i:i+2]가 두 자리수 가능하면 (11-26 사이, i+2가 0이 아님)
dp[i] += f(i+2)
f(i) = f(i+1) + f(i+2)
'''
import sys
sys.setrecursionlimit(10**6)

s = str(input())
one = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
two = {'10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'}
s += '.'
memo = {}
def f(i):
    if i >= len(s)-1:
        return 1
    
    if i in memo:
        return memo[i]
    
    memo[i] = 0
    if i + 1 <= len(s):
        if s[i] in one and s[i+1] != 0:
            memo[i] += f(i+1)
    if i + 2 <= len(s):
        if s[i:i+2] in two and s[i+2] != 0:
            memo[i] += f(i+2)
    
    return memo[i]

print(f(0) % 1000000)