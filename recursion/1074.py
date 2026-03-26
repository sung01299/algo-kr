"""
base case (n==1):
(0,0) (0,1) (1,0) (1,1)

n == 2:
(0,0) (0,1) (1,0) (1,1) -> (0,2) (0,3) (1,2) (1,3)
-> (2,0) (2,1) (3,0) (3,1) -> (2,2) (2,3) (3,2) (3,3)

+2, +2, +2
"""

n, r, c = map(int, input().split())

def f(n, r, c):
    if n == 0:
        return 0
    half = 2 ** (n-1)
    # 1
    if (r < half and c < half):
        return f(n-1, r, c)
    # 2
    if (r < half and c >= half):
        return half*half + f(n-1, r, c-half)
    # 3
    if (r >= half and c < half):
        return 2*half*half + f(n-1, r-half, c)
    # 4
    return 3*half*half + f(n-1, r-half, c-half)

print(f(n,r,c))