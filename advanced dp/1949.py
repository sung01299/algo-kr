from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

'''
dp[i][incl] = dp[nxt][not incl]
dp[i][not incl] = max(dp[nxt][incl], dp[nxt][not incl])
'''

n = int(input())
nums = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dp = [[0, 0] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def f(i):
    visited[i] = True
    dp[i][1] = nums[i-1]

    for nxt in graph[i]:
        if not visited[nxt]:
            f(nxt)

            dp[i][1] += dp[nxt][0]
            dp[i][0] += max(dp[nxt][1], dp[nxt][0])

f(1)
print(max(dp[1][0], dp[1][1]))