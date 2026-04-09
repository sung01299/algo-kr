'''
1 -> 1
2 -> 1+1, 2
3 -> 1+1+1, 2+1, 3
4 -> 1+1+1+1, 2+1+1, 2+2, 3+1
5 -> 1+1+1+1+1, 2+1+1+1, 2+2+1, 3+1+1, 3+2
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    for num in range(1, 4):
        for i in range(1, n+1):
            if i >= num:
                if i == num:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-num]
    
    print(dp[-1])