from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque()
ans = []
l, r = -L+1, 0

for i in range(l, r+1):
    queue.append(nums[i])
ans.append(min(queue))

while r < N:
    queue.popleft()
    queue.append(nums[r])
    r += 1
    ans.append(min(queue))

print(*ans)