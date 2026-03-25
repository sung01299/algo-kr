s = str(input())

alphabet = [0 for _ in range(26)]

for c in s:
    alphabet[ord(c) - 97] += 1

for idx in range(26):
    print(alphabet[idx], end=' ')