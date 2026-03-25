a = int(input())
b = int(input())
c = int(input())

digits = [0 for _ in range(10)]
res = a * b * c

for c in str(res):
    digits[int(c)] += 1

for idx in range(10):
    print(digits[idx])