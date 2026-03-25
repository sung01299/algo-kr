"""
[6] -> 6: 0
[9] -> 9: 0
[9, 5] -> 5: (9)
[9, 7] -> 7: (9)
[9, 7, 4] -> 4: (7)
"""

import sys

N = int(sys.stdin.readline())
towers = list(map(int, input().split()))

stack = [0] # store indexes, monotonically decreasing stack
ans = [0]

for idx in range(1, N):
    while stack and towers[idx] > towers[stack[-1]]:
        stack.pop()
    if stack:
        ans.append(stack[-1] + 1)
    else:
        ans.append(0)
    stack.append(idx)


print(*ans)