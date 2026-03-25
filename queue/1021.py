"""
1 2 3 4 5 6 7 8 9 10

2 -> left 1, 3 4 5 6 7 8 9 10 1, right 9
9 -> right 3 -> 9 10 1 3 4 5 6 7 8, left 6
5 -> 
"""
from collections import deque
N, M = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque()

for i in range(1, N+1):
    queue.append(i)

def to_left():
    top = queue.popleft()
    queue.append(top)

def to_right():
    bot = queue.pop()
    queue.appendleft(bot)

ans = 0
for num in nums:
    cnt = 0
    while queue[0] != num:
        to_left()
        cnt += 1
    ans += min(cnt, len(queue) - cnt)
    queue.popleft()

print(ans)