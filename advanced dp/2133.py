n = int(input())

if n % 2 == 1:
    print(0)
else:
    memo = {2: 3}
    def f(i):
        if i <= 0:
            return 0
        if i in memo:
            return memo[i]
        
        memo[i] = f(i-2) * 3 + 2 # + f(i-4) * 2 + f(i-6) * 2 + ... + 2
        for n in range(i-4, -1, -2):
            memo[i] += f(n) * 2

        return memo[i]
    
    print(f(n))