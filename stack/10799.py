stack = []
ans = 0

s = str(input())

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)