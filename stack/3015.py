"""
[4, 3, 2, 1, 1, 2, 4]
[4]
[4, 3]
[4, 3, 2]
[4, 3, 2, 1]
[4, 3, 2, 1(2)]
[4, 3, 2, 1] 1 -> 1
[4, 3, 2] 1 -> 2
[4, 3, 2(2)]
[4, 3, 2] 2 -> 1
[4, 3] 2 -> 4
[4] 3 -> 5
[4, 4] -> finish, 1
total: 14

"""

import sys
input = sys.stdin.readline

N = int(input())
heights = []
for _ in range(N):
    h = int(input())
    heights.append(h)

stack = [0]
ans = 0

for idx in range(1, N):
    while stack and heights[idx] > heights[stack[-1]]:
        rmv = stack.pop()
        ans += (idx - rmv)
        print(ans, rmv, idx - rmv)
    stack.append(idx)

print(stack)
#　마지막 계산
print(ans)
