"""
https://www.acmicpc.net/problem/11723
"""

import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    t = sys.stdin.readline().strip().split()

    if len(t) == 1:
        if t[0] == "all":
            s = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
        else:
            s = set()
    
    else:
        cmd, num = t[0], t[1]
        num = int(num)

        if cmd == "add":
            s.add(num)
        elif cmd == "remove":
            s.discard(num)
        elif cmd == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)
        else:
            print(1 if num in s else 0)