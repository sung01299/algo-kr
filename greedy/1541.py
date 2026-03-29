'''
- 후 최대한 많은 + 연산
'''
n = []
ipt = str(input())
num = ''
for i in ipt:
    if i == '-' or i == '+':
        n.append(int(num))
        n.append(i)
        num = ''
    else:
        num += i
n.append(int(num))

ans = n[0]
minus = False
tmp = 0
for i in range(1, len(n)):
    if n[i] == '-':
        minus = False
        ans -= tmp
        tmp = 0
        minus = True
    elif n[i] == '+':
        continue
    else:
        if minus:
            tmp += n[i]
        else:
            ans += n[i]

ans -= tmp
print(ans)
