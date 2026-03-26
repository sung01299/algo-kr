n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

path = []
issued = [False for _ in range(n)]
def f(depth):
    if depth == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(n):
        if not issued[i]:
            path.append(nums[i])
            issued[i] = True
            f(depth + 1)
            path.pop()
            issued[i] = False

f(0)