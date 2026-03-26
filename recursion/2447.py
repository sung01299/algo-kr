n = int(input())

board = [[' ' for _ in range(n)] for _ in range(n)]

def f(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == 3:
                if i * j != 1:
                    board[x+i][y+j] = '*'
            else:
                if i* j != 1:
                    f(x + i*(n // 3), y + j*(n // 3), n // 3)

f(0, 0, n)
for row in board:
    print(''.join(row))