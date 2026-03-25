"""
괄호 안의 값을 어떻게 계산할것인가
값/연산이 확정되는 순간은 괄호가 닫힐 때 -> pop후, 계산한 숫자 추가
() -> 2, [] -> 3, ( x ) -> 2*x, [ x ] -> 3*x, xy -> x + y
tmp 값이 필요한가?, stack에다가 괄호, 숫자도 넣기?
(,2,9,) -> 22
"""
hashmap = {")":"(", "]":"["}
values = {")": 2, "]": 3}
stack = []
s = str(input())
error = False

for i in range(len(s)):
    if s[i] == "(" or s[i] == "[":
        stack.append(s[i])
    else:
        # () or []
        if s[i-1] == hashmap[s[i]]:
            stack.pop()
            stack.append(values[s[i]])
        else:
            tmp = 0
            if not isinstance(stack[-1], int) and stack[-1] != hashmap[s[i]]:
                error = True
                break
            while stack[-1] != hashmap[s[i]]:
                num = stack.pop()
                tmp += num
            rm = stack.pop()
            stack.append(tmp * values[s[i]])

print(sum(stack) if not error else 0)
