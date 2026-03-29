n = int(input())

neg = []
pos = []
one = []
for _ in range(n):
    i = int(input())
    if i > 1:
        pos.append(i)
    elif i == 1:
        one.append(i)
    else:
        neg.append(i)

neg.sort()
pos.sort(reverse=True)

ans = 0
for i in range(0, len(pos), 2):
    if i+1 <= len(pos) - 1:
        ans += (pos[i] * pos[i+1])
    else:
        ans += pos[i]

for i in range(0, len(neg), 2):
    if i+1 <= len(neg) - 1:
        ans += (neg[i] * neg[i+1])
    else:
        ans += neg[i]

ans += sum(one)

print(ans)