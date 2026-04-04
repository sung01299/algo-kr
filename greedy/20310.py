from collections import Counter

s = str(input())
s_arr = [c for c in s]
counter = Counter(s)

for k, v in counter.items():
    counter[k] = v // 2

for i in range(len(s_arr)):
    if s_arr[i] == '1' and counter['1'] > 0:
        s_arr[i] = -1
        counter['1'] -= 1

for i in range(len(s_arr) - 1, -1, -1):
    if s_arr[i] == '0' and counter['0'] > 0:
        s_arr[i] = -1
        counter['0'] -= 1

ans = ''
for c in s_arr:
    if c != -1:
        ans += c

print(ans)