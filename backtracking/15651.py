n, m = map(int, input().split())

path = []
def f(k):
    if k == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, n+1):
        path.append(i)
        f(k+1)
        path.pop()

f(0)