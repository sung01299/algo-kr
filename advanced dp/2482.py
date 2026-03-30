n = int(input())
k = int(input())

'''
i에서 시작해서 고를 수 있는 갯수
f(i) = f(i+1) + f(i+2)
'''

memo = {}
def f(i, cnt):
    if cnt > k or i >= n:
        return 0
    if cnt == k:
        return 1
    
    if (i, cnt) in memo:
        return memo[(i, cnt)]
    
    memo[(i, cnt)] = f(i+1, cnt) + f(i+1, cnt+1)
    memo[(i, cnt+1)] = f(i+2, cnt) + f(i+2, cnt+2)

    return memo[(i, cnt)]

f(0, 0)
print(memo[(0,0)] + memo[(0,1)])