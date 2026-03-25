import sys

n = int(sys.stdin.readline())

stack = []
cur_count = 1
cmds = []
fail = False

for _ in range(n):
    num = int(sys.stdin.readline())
    while num >= cur_count:
        cmds.append("+")
        stack.append(cur_count)
        cur_count += 1
    
    if stack[-1] == num:
        stack.pop()
        cmds.append("-")
    else:
        fail = True
        break

if fail:
    print("NO")
else:
    for elem in cmds:
        print(elem)