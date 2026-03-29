s = str(input())
s += '..'

c1 = {'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='}

i = 0
ans = 0
while i < len(s):
    if s[i:i+2] in c1:
        ans += 1
        i += 2
    elif s[i:i+3] == 'dz=':
        ans += 1
        i += 3
    else:
        i += 1
        ans += 1

print(ans-2)