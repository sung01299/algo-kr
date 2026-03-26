n, m = map(int, input().split())

path = []
def f(start, depth):
    if depth == m:
        print(' '.join(map(str, path)))
        return

    for i in range(start, n+1):
        path.append(i)
        f(i, depth+1)
        path.pop()

f(1, 0)