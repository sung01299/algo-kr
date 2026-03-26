n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
ans = set()
issued = [False for _ in range(n)]

def f(start, depth):
    if depth == m:
        t = ' '.join(map(str, path))
        if t not in ans:
            print(t)
            ans.add(t)
        return
    
    for i in range(start, n):
        if not issued[i]:
            issued[i] = True
            path.append(nums[i])
            f(i, depth+1)
            issued[i] = False
            path.pop()

f(0, 0)