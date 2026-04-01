import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())
ls = list(map(int, input().split()))

def get_diff():
    diffs = [abs(0 - ls[0])]
    for i in range(1, m):
        diffs.append(math.ceil(abs(ls[i] - ls[i-1]) / 2))
    diffs.append(n - ls[-1])
    
    return diffs

def solve():
    diffs = get_diff()
    print(max(diffs))

solve()
