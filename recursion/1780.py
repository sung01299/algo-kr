"""
Basecase:
if n == 1:
    나눌 필요 없음
    각 숫자별 + 1
    return 1

if n == 2: (3x3):
    check if all same,
    if yes: return 1
    if no:
        9개 칸에 대해
        f(n-1)

"""
from collections import defaultdict
n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

ans = defaultdict(int)

def f(x, y, k):
    color = board[x][y]

    for r in range(x, x+k):
        for c in range(y, y+k):
            if color != board[r][c]:
                for i in range(3):
                    for j in range(3):
                        f(x + (k // 3)*i, y + (k // 3)*j, k // 3)
                return
    
    ans[color] += 1

f(0, 0, n)

print(ans[-1])
print(ans[0])
print(ans[1])