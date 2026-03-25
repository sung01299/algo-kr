import sys
# input = sys.stdin.readline
hash = {")":"(", "]": "["}

while True:
    s = input()
    stack = []
    ans = "yes"
    if s == '.':
        break
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")" or c == "]":
            if stack and stack[-1] == hash[c]:
                stack.pop()
            else:
                ans = "no"
    if stack:
        ans = "no"
    print(ans)