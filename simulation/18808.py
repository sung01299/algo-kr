import copy


n, m, k = map(int, input().split())
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    # [r, c, [sticker]]
    sticker = [r, c, []]
    for _ in range(r):
        row = list(map(int, input().split()))
        sticker[2].append(row)
    stickers.append(sticker)

board = [[0 for _ in range(m)] for _ in range(n)]

def rot90(sticker):
    r, c, s = sticker
    new = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new[j][r-i-1] = s[i][j]
    return [c, r, new]

def extract_positions(sticker):
    res = []
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                res.append((i,j))
    return res

def can_patch(sticker, b_r, b_c, board, coordinates):
    for i, j in coordinates:
        if sticker[i][j] == 1 and board[b_r+i][b_c+j] == 1:
            return False
    return True

def patch(sticker, b_r, b_c, board, coordinates):
    for i, j in coordinates:
        if sticker[i][j] == 1:
            board[b_r+i][b_c+j] = 1
    
    return board

def calculate(board):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                cnt += 1
    
    return cnt

def check(s, r, c, prev_board, coordinates):
    res, b = False, []
    for row in range(n-r+1):
        for col in range(m-c+1):
            res = can_patch(s, row, col, prev_board, coordinates)
            if res:
                b = patch(s, row, col, prev_board, coordinates)
                return res, b
    
    return res, b

# patch stickers one by one to board
for idx in range(len(stickers)):
        
    # 1. original
    r, c, s = stickers[idx]
    prev_board = copy.deepcopy(board)
    complete = False
    coordinates = extract_positions(s)

    # from top to bottom, left to right
    res, b = check(s, r, c, prev_board, coordinates)
    if res:
        complete = True
        board = b
        continue

    # 2. 90 rot
    if not complete:
        rot1 = rot90(stickers[idx])
        r, c, s = rot1
        coordinates = extract_positions(s)
        res, b = check(s, r, c, prev_board, coordinates)
        if res:
            complete = True
            board = b
            continue

    # 3. 180 rot
    if not complete:
        rot2 = rot90(rot1)
        r, c, s = rot2
        coordinates = extract_positions(s)
        res, b = check(s, r, c, prev_board, coordinates)
        if res:
            complete = True
            board = b
            continue

    # 4. 270 rot
    if not complete:
        rot3 = rot90(rot2)
        r, c, s = rot3
        coordinates = extract_positions(s)
        res, b = check(s, r, c, prev_board, coordinates)
        if res:
            complete = True
            board = b
            continue
        
print(calculate(board))