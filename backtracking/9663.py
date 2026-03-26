n = int(input())

cnt = 0
arr = [0 for _ in range(n)]
issued1 = [False for _ in range(n)]
issued2 = [False for _ in range(2*n-1)]
issued3 = [False for _ in range(2*n-1)]

def f(k):
    global cnt
    if k == n:
        cnt += 1
        return
    
    for i in range(n):
        if issued1[i] or issued2[k+i] or issued3[k-i+n-1]:
            continue
        issued1[i] = True
        issued2[k+i] = True
        issued3[k-i+n-1] = True
        f(k+1)
        issued1[i] = False
        issued2[k+i] = False
        issued3[k-i+n-1] = False

f(0)
print(cnt)