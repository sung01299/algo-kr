from collections import deque

board = []
for _ in range(5):
    row = [c for c in input()]
    board.append(row)

print(board)

# Q = deque()
# visited = 
path = []

def f(depth):
    if depth == 7:
        print(path)
        return
    
    # for i in 
