"""
BAABBB
AB
if stack is empty or last element is not same, append
if last element is same, pop
finally, check if stack is empty
"""


N = int(input())
ans = 0
for _ in range(N):
    word = str(input())
    stack = []
    for c in word:
        if not stack or stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
    if not stack:
        ans += 1

print(ans)