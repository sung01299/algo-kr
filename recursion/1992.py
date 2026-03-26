n = int(input())
board = []
for _ in range(n):
    row = [int(c) for c in input()]
    board.append(row)

ans = []

def f(x, y, k):
    color = board[x][y]

    for r in range(x, x+k):
        for c in range(y, y+k):
            if color != board[r][c]:
                ans.append("(")
                for i in range(2):
                    for j in range(2):   
                        f(x + i*(k//2), y + j*(k//2), k // 2)
                ans.append(")")
                return

    ans.append(str(color))

f(0, 0, n)
print(''.join(ans))