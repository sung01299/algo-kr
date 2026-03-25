import sys
input = sys.stdin.readline

"""
[10]
[10, 3]
[10, 7] -> 3: idx(7) - idx(3) = 1 (itself)
[10, 7, 4]
[10, 7] -> 4: idx(12) - idx(4) = 1 (itself)
[10] -> 7: idx(12) - idx(7) = 2 (1 visible)
[12] -> 10: idx(12) - idx(10) = 4 (3 visible)
[12, 6]

for remaining:
    if [a,b] -> b (1)
    if [a, b, c] -> bc, c (3)
    if [a, b, c, d] -> bcd, cd, d (6)
"""

N = int(input())
heights = []
ans = 0

stack = [0] # stores indices, monotonic decreasing stack
for _ in range(N):
    h = int(input())
    heights.append(h)

for idx in range(1, N):
    while stack and heights[idx] >= heights[stack[-1]]:
        rmved_idx = stack.pop()
        ans += (idx - rmved_idx - 1)
    stack.append(idx)

for idx in stack:
    ans += len(heights) - idx - 1
    
print(ans)