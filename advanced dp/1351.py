n, p, q = map(int, input().split())

dp = {}
def f(i):
    if i == 0:
        return 1
    if i in dp:
        return dp[i]
    
    a = i // p
    b = i // q
    dp[i] = f(a) + f(b) 
    return dp[i]

print(f(n))