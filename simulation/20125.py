n = int(input())

board = []
for _ in range(n):
    row = []
    r = str(input())
    for c in r:
        row.append(c)
    board.append(row)

def get_head():
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                return i, j

def get_left_arm(x, y):
    cnt = 0
    for i in range(y-1, -1, -1):
        if board[x][i] == '_':
            return cnt
        else:
            cnt += 1
    return cnt

def get_right_arm(x, y):
    cnt = 0
    for i in range(y+1, n):
        if board[x][i] == '_':
            return cnt
        else:
            cnt += 1
    return cnt

def get_waist(x, y):
    cnt = 0
    end = x
    for i in range(x+1, n):
        if board[i][y] == '_':
            end = i-1
            return cnt, end, y
        else:
            cnt += 1
    return cnt, end, y

def get_left_leg(x, y):
    cnt = 0
    s_x, s_y = x+1, y-1
    for i in range(s_x, n):
        if board[i][s_y] == '_':
            return cnt
        else:
            cnt += 1
    return cnt

def get_right_leg(x, y):
    cnt = 0
    s_x, s_y = x+1, y+1
    for i in range(s_x, n):
        if board[i][s_y] == '_':
            return cnt
        else:
            cnt += 1
    return cnt

def solve():       
    head_x, head_y = get_head()
    heart_x, heart_y = head_x+1, head_y
    left_arm = get_left_arm(heart_x, heart_y)
    right_arm = get_right_arm(heart_x, heart_y)
    waist, w_end_x, w_end_y = get_waist(heart_x, heart_y)
    left_leg = get_left_leg(w_end_x, w_end_y)
    right_leg = get_right_leg(w_end_x, w_end_y)

    print(heart_x+1, heart_y+1)
    print(left_arm, right_arm, waist, left_leg, right_leg)

solve()