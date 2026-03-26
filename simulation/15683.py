"""
1 -> 1 side       | 4 choices
2 -> 2 sides (<>) | 2 choices
3 -> 2 sides (ㄴ)  | 4 choices
4 -> 3 sides (|-) | 4 choices
5 -> all sides    | 1 choice
6 -> wall
"""
from collections import defaultdict
n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

cctv = []
cctv5list = []
for r in range(n):
    for c in range(m):
        if board[r][c] >= 1 and board[r][c] <= 4:
            cctv.append((board[r][c], r, c))
        if board[r][c] == 5:
            cctv5list.append((r, c))
    
mode = [
    [''],
    ['up', 'down', 'right', 'left'],
    ['up', 'down'],
    ['up', 'down', 'right', 'left'],
    ['up', 'down', 'right', 'left'],
    ['up', 'down', 'right', 'left']
]

# dir: up, down, right, left
def cctv1(direction, x, y, board):
    n_board = board
    if direction == 'up':
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    elif direction == 'down':
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    elif direction == 'right':
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    else: # left
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    return n_board

def cctv2(direction, x, y, board):
    n_board = board
    if direction == 'up':
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    else: # left
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    return n_board

def cctv3(direction, x, y, board):
    n_board = board
    if direction == 'up': # up, right
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    elif direction == 'right': # right, down
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    elif direction == 'down': # down, left
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    else: # left, up
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    return n_board

def cctv4(direction, x, y, board):
    n_board = board
    if direction == 'up': # left, up, right
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    elif direction == 'right': # up, right, down
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    elif direction == 'down': # right, down, left
        for i in range(y+1, m):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
    else: # down, left, up
        for i in range(x+1, n):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
        for i in range(y-1, -1, -1):
            if n_board[x][i] == 6:
                break
            if n_board[x][i] != 0:
                continue
            if n_board[x][i] != 6:
                n_board[x][i] = '#'
        for i in range(x-1, -1, -1):
            if n_board[i][y] == 6:
                break
            if n_board[i][y] != 0:
                continue
            if n_board[i][y] != 6:
                n_board[i][y] = '#'
    return n_board
        
def cctv5(x, y, board):
    n_board = board
    for i in range(x-1, -1, -1):
        if n_board[i][y] == 6:
            break
        if n_board[i][y] != 0:
            continue
        if n_board[i][y] != 6: 
            n_board[i][y] = '#'
    for i in range(x+1, n):
        if n_board[i][y] == 6:
            break
        if n_board[i][y] != 0:
            continue
        if n_board[i][y] != 6:
            n_board[i][y] = '#'
    for i in range(y+1, m):
        if n_board[x][i] == 6:
            break
        if n_board[x][i] != 0:
            continue
        if n_board[x][i] != 6:
            n_board[x][i] = '#'
    for i in range(y-1, -1, -1):
        if n_board[x][i] == 6:
            break
        if n_board[x][i] != 0:
            continue
        if n_board[x][i] != 6:
            n_board[x][i] = '#'
    return n_board
        
def calculate(board):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt

for x, y in cctv5list:
    board = cctv5(x, y, board)

ans = float('inf')
def simulate(cnt, board):
    global ans
    if cnt == len(cctv):
        # print('!!')
        # for r in board:
        #     print(' '.join(map(str, r)))
        ans = min(ans, calculate(board))
        return

    last_board = [[j for j in board[i]] for i in range(n)]

    cctv_num, x, y = cctv[cnt]
    for direction in mode[cctv_num]:
        if cctv_num == 1:
            cctv1(direction, x, y, last_board)
        elif cctv_num == 2:
            cctv2(direction, x, y, last_board)
        elif cctv_num == 3:
            cctv3(direction, x, y, last_board)
        elif cctv_num == 4:
            cctv4(direction, x, y, last_board)
        simulate(cnt+1, last_board)
        last_board = [[j for j in board[i]] for i in range(n)]

simulate(0, board)
print(ans)