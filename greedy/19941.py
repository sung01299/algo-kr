'''
최대한 멀리 떨어진 왼쪽 햄버거 먹기
'''
n, k = map(int, input().split())
p = []
hp = [c for c in str(input())]

ans = 0
for idx in range(n):
    if hp[idx] == 'P':
        for i in range(max(0, idx-k), min(n, idx+k+1)):
            if hp[i] == 'H':
                hp[i] = 0
                ans += 1
                break

print(ans)