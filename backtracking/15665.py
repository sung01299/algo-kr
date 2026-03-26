n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
ans = set()

def f(depth):
    if depth == m:
        t = ' '.join(map(str, path))
        if t not in ans:
            ans.add(t)
            print(t)
        return
    
    for i in range(n):
        path.append(nums[i])
        f(depth + 1)
        path.pop()

f(0)