n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
def f(depth):
    if depth == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(n):
        path.append(nums[i])
        f(depth+1)
        path.pop()

f(0)