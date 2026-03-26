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

                for i in range(2):
                    for j in range(2):
                        f(x + i*(k//2), y + j*(k//2), k//2)
                return
    
    ans[color] += 1

f(0, 0, n)
print(ans[0])
print(ans[1])