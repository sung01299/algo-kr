n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
def f(start, depth):
    if depth == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(start, n):
        path.append(nums[i])
        f(i+1, depth+1)
        path.pop()

f(0, 0)