import sys
from collections import deque
# input = sys.stdin.readline

def reverse(arr):
    return deque(list(reversed(arr)))


T = int(input())
for _ in range(T):
    cmds = str(input())
    n = int(input())
    error = False
    rev = False
    ipt = input()
    ipt = ipt[1:len(ipt)-1]
    ipt = ipt.split(',')
    queue = deque(ipt)

    for cmd in cmds:
        if cmd == "R":
            rev = not rev
        
        elif n != 0:
            if rev:
                queue.pop()
                n -= 1
            else:
                queue.popleft()
                n -= 1
        else:
            error = True

    queue = list(queue)
    if error:
        print("error")
    else:
        res = '[' + ','.join(queue[::-1]) + ']' if rev else '[' + ','.join(queue) + ']'
        print(res)



