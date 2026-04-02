'''
distance: 0 2 5 6
1st approach: backtracking
2nd approach: greedy
- maximize oil purchase at lower price
'''
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
prefix = [0]
for i in range(n-1):
    prefix.append(dist[i] + prefix[-1])

# ans = float('inf')
# def f(i, total):
#     global ans
#     if i == n-1:
#         ans = min(ans, total)
#         return
    
#     for nxt in range(i+1, n):
#         total += price[i] * (prefix[nxt] - prefix[i])
#         f(nxt, total)
#         total -= price[i] * (prefix[nxt] - prefix[i])

# f(0, 0)
# print(ans)

ans = 0
cur = 0
end = 0
while cur < n - 1 and end < n - 1:
    if price[cur] <= price[end]:
        end += 1
    else:
        ans += (prefix[end] - prefix[cur]) * price[cur]
        cur = end

ans += (prefix[end] - prefix[cur]) * price[cur]
print(ans)