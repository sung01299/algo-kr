n, m = map(int, input().split())

arr = [0 for _ in range(n)]
issued = [False for _ in range(n)]

def f(k):
    if k == m:
        for i in range(m):
            print(arr[i])
        return

    for i in range(1, n+1):
        if not issued[i-1]:
            arr[k] = i
            issued[i-1] = True
            f(k+1)
            issued[i-1] = False

f(0)