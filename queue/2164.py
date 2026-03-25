from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
if N == 1:
    print(1)
else:
    for i in range(1, N+1):
        queue.append(i)

    while queue:
        queue.popleft()
        if len(queue) == 1:
            print(queue[0])
            break
        top = queue.popleft()
        queue.append(top)
