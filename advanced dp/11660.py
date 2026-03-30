'''
그냥 바로 든 생각:
row 별 prefix 구해서 계산하기
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    prefix = [0]
    row = list(map(int, input().split()))
    for i, val in enumerate(row):
        prefix.append(prefix[i] + val)
    board.append(prefix)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for row in range(x1-1, x2):
        ans += board[row][y2] - board[row][y1-1]
    
    print(ans)