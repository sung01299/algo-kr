T = int(input())
for _ in range(T):
    stack = []
    s = str(input())
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
    if stack:
        print("NO")
    else:
        print("YES")