"""
[3,5,2,7]
[3]
[5] -> 3: 5
[5, 2]
[5] -> 2: 7
[7] -> 5: 7

[9,5,4,8]
[9]
[9, 5]
[9, 5, 4]
[9, 5] -> 4: 8
[9] -> 5: 8
[8] -> 9: 8
"""
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
ans = [-1 for _ in range(N)]

stack = [0] # stores indices, monotonic decreasing stack
for idx in range(1, N):
    while stack and a[idx] > a[stack[-1]]:
        rmv = stack.pop()
        ans[rmv] = a[idx]
    stack.append(idx)

print(*ans)
