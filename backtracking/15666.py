n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
ans = set()

def f(start, depth):
    if depth == m:
        t = ' '.join(map(str, path))
        if t not in ans:
            ans.add(t)
            print(t)
        return
    
    for i in range(start, n):
        path.append(nums[i])
        f(i, depth+1)
        path.pop()

f(0, 0)