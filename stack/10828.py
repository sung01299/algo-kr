n = int(input())

stack = []
for _ in range(n):
    cmdnum = input()
    if cmdnum == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmdnum == "empty":
        print(0 if stack else 1)
    elif cmdnum == "pop":
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif cmdnum == "size":
        print(len(stack))
    else:
        cmd, num = cmdnum.split()
        stack.append(num)
