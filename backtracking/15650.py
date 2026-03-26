n, m = map(int, input().split())

arr = [0 for _ in range(m)]
# issued = [False for _ in range(n)]

# def f(k, path, cur):
#     if k == m:
#         print(' '.join(path))
#         return

#     for i in range(k, n):
#         if not issued[i] and cur <= i:
#             path.append(str(i + 1))
#             issued[i] = True
#             f(k+1, path, i)
#             path.pop()
#             issued[i] = False

# f(0, [], 0)

def f(k, path):
    print(path)
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(k, n+1):
        path.append(i)
        f(k+1, path)
        path.pop()

f(0, [])
