n, s = map(int, input().split())
nums = list(map(int, input().split()))
 
cnt = 0
arr = [0 for _ in range(n)]

def f(k, total):
    global cnt
    if k == n:
        if total == s:
            cnt += 1
        return
    f(k+1, total)
    f(k+1, total + nums[k])

f(0, 0)
print(cnt if s != 0 else cnt - 1)
