s = str(input())

cnt = 0
idx = 0

while True:
    cnt += 1
    for c in str(cnt):
        if s[idx] == c:
            idx += 1
            if idx >= len(s):
                print(cnt)
                exit()